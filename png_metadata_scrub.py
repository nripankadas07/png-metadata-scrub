"""Remove selected PNG metadata chunks while retaining all other encoded bytes."""
import argparse, hashlib, json, pathlib, struct, zlib
SIGNATURE=b"\x89PNG\r\n\x1a\n"
REMOVE={b"tEXt",b"zTXt",b"iTXt",b"eXIf",b"tIME"}
def scrub(data):
    if len(data)>32*1024*1024 or not data.startswith(SIGNATURE):raise ValueError("not a PNG or exceeds 32 MiB")
    pos=8;chunks=[];seen_idat=False;closed_idat=False;ended=False;palette=False;colour=None;removed=[];out=[SIGNATURE]
    while pos<len(data):
        if ended or pos+12>len(data):raise ValueError("trailing or truncated chunk")
        size=struct.unpack(">I",data[pos:pos+4])[0];kind=data[pos+4:pos+8];end=pos+12+size
        if end>len(data) or not all(65<=c<=90 or 97<=c<=122 for c in kind) or kind[2]&32:raise ValueError("invalid chunk length or type")
        payload=data[pos+8:pos+8+size];crc=struct.unpack(">I",data[end-4:end])[0]
        if zlib.crc32(kind+payload)&0xffffffff!=crc:raise ValueError("CRC mismatch")
        if not chunks:
            if kind!=b"IHDR" or size!=13:raise ValueError("IHDR must be first, length 13")
            w,h,depth,colour,comp,filt,inter=struct.unpack(">IIBBBBB",payload)
            legal={0:{1,2,4,8,16},2:{8,16},3:{1,2,4,8},4:{8,16},6:{8,16}}
            if not w or not h or w>2**31-1 or h>2**31-1 or depth not in legal.get(colour,set()) or comp or filt or inter not in (0,1):raise ValueError("invalid IHDR")
        elif kind==b"IHDR":raise ValueError("duplicate IHDR")
        if kind==b"PLTE":
            if palette or seen_idat or colour in (0,4) or not size or size%3 or size>768:raise ValueError("invalid PLTE")
            if colour==3 and size//3>2**depth:raise ValueError("palette exceeds indexed bit depth")
            palette=True
        if kind==b"IDAT":
            if closed_idat or (colour==3 and not palette):raise ValueError("invalid IDAT order")
            seen_idat=True
        elif seen_idat:closed_idat=True
        if kind==b"IEND":
            if size or not seen_idat:raise ValueError("invalid IEND or missing IDAT")
            ended=True
        if not kind[0]&32 and kind not in {b"IHDR",b"PLTE",b"IDAT",b"IEND"}:raise ValueError("unsupported critical chunk")
        if kind in {b"acTL",b"fcTL",b"fdAT"}:raise ValueError("APNG unsupported")
        chunks.append(kind.decode())
        if len(chunks)>10000:raise ValueError("more than 10000 chunks")
        if kind in REMOVE:removed.append({"type":kind.decode(),"bytes":size})
        else:out.append(data[pos:end])
        pos=end
    if not ended:raise ValueError("missing IEND")
    clean=b"".join(out)
    return clean,{"removed":removed,"retained_chunks":[x for x in chunks if x.encode() not in REMOVE],"input_bytes":len(data),"output_bytes":len(clean),"input_sha256":hashlib.sha256(data).hexdigest(),"output_sha256":hashlib.sha256(clean).hexdigest(),"pixel_stream_reencoded":False}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input");p.add_argument("output");a=p.parse_args()
    try:
        data=pathlib.Path(a.input).read_bytes();clean,r=scrub(data)
        with pathlib.Path(a.output).open("xb") as f:f.write(clean)
        print(json.dumps(r));return 0
    except (ValueError,OSError) as e:print(json.dumps({"error":str(e)}));return 2
if __name__=="__main__":raise SystemExit(main())
