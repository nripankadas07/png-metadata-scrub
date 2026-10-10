import struct,zlib,unittest
from png_metadata_scrub import scrub,SIGNATURE
def chunk(k,b):return struct.pack(">I",len(b))+k+b+struct.pack(">I",zlib.crc32(k+b)&0xffffffff)
IHDR=chunk(b"IHDR",struct.pack(">IIBBBBB",1,1,8,2,0,0,0));IDAT=chunk(b"IDAT",zlib.compress(b"\0\xff\0\0"));IEND=chunk(b"IEND",b"")
def png(extra=b""):return SIGNATURE+IHDR+extra+IDAT+IEND
class Contract(unittest.TestCase):
    def test_remove_all_selected(self):
        extra=b"".join(chunk(k,b"private") for k in [b"tEXt",b"iTXt",b"zTXt",b"eXIf",b"tIME"]);clean,r=scrub(png(extra));self.assertEqual(clean,png());self.assertEqual(len(r["removed"]),5)
    def test_idempotence(self):
        clean,_=scrub(png(chunk(b"tEXt",b"secret")));self.assertEqual(scrub(clean)[0],clean)
    def test_idat_exact(self):self.assertIn(IDAT,scrub(png())[0])
    def test_colour_metadata(self):
        data=png(chunk(b"gAMA",struct.pack(">I",45455)));self.assertEqual(scrub(data)[0],data)
    def test_unknown_ancillary_preserved(self):
        data=png(chunk(b"vpAg",b"unrecognized"));self.assertEqual(scrub(data)[0],data)
    def test_report_no_payload(self):self.assertNotIn("secret",str(scrub(png(chunk(b"tEXt",b"secret")))[1]))
    def test_bad_crc(self):
        with self.assertRaises(ValueError):scrub(png()[:-1]+b"x")
    def test_truncated(self):
        with self.assertRaises(ValueError):scrub(png()[:-3])
    def test_trailing(self):
        with self.assertRaises(ValueError):scrub(png()+b"x")
    def test_duplicate_ihdr(self):
        with self.assertRaises(ValueError):scrub(png(IHDR))
    def test_apng(self):
        with self.assertRaises(ValueError):scrub(png(chunk(b"acTL",b"12345678")))
    def test_critical_unknown(self):
        with self.assertRaises(ValueError):scrub(png(chunk(b"ABCD",b"")))
    def test_missing_idat(self):
        with self.assertRaises(ValueError):scrub(SIGNATURE+IHDR+IEND)
    def test_nonconsecutive_idat(self):
        with self.assertRaises(ValueError):scrub(SIGNATURE+IHDR+IDAT+chunk(b"tEXt",b"a")+IDAT+IEND)
