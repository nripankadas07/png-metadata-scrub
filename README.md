# png-metadata-scrub

Validate bounded PNG chunk framing/CRCs and key structural ordering, remove tEXt/zTXt/iTXt/eXIf/tIME, retain every other encoded chunk byte-for-byte, and write only to a new output path.

## Who and why

Asset handoff reviewers removing specific text, EXIF and time chunks while preserving the encoded image stream. An image optimizer can reencode pixels or remove display metadata. A review needs an exact account of which metadata was removed and a refusal to overwrite an existing file.

## Quickstart

Python 3.10+ and pip. No service, credential or runtime dependency:

```sh
git clone https://github.com/nripankadas07/png-metadata-scrub.git
cd png-metadata-scrub
python -m venv .venv
# Unix: source .venv/bin/activate; Windows: .venv\Scripts\activate
python -m pip install .
png-metadata-scrub sample.png clean.png
python demo.py
python -m pip install setuptools wheel
python verify.py
```

The fixtures are synthetic. CLI JSON is on stdout. Exit 0 means the operation succeeded; HLS/mbox return 1 for findings; all tools return 2 for malformed/unsupported input or IO errors. SQLite scan signals are evidence, not policy failures. PNG output must be a new file: repeating its command requires a new output filename.

Help: `png-metadata-scrub --help`. See [DEMO.md](DEMO.md), [VALIDATION.md](VALIDATION.md), [RESEARCH.md](RESEARCH.md) and [SUPPORT.md](SUPPORT.md).

## Scope and limitations

Not a decoder, image optimizer, full PNG conformance validator or complete privacy guarantee. IDAT is not decompressed or validated; malicious pixel streams can survive. Unknown ancillary chunks and colour profiles remain and can contain identifying data. Pixel content itself may identify a person. APNG and unknown critical chunks are rejected. Some ancillary ordering/content constraints are not checked. 32 MiB, 10,000 chunks. A filesystem write failure can leave a partial new output; existing outputs are never overwritten.

No performance-superiority or complete-security claim. Use the comparable research to choose a tool suitable for your workflow.

## License

MIT; original implementation. Build-time setuptools/wheel and Python retain their upstream licenses.
