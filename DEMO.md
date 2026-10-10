# Synthetic demo

Run `python demo.py` to exercise the checked-in synthetic fixture, expected success/evidence and malformed input using `smoke.json`.

Installed command: `png-metadata-scrub sample.png clean.png`. Each smoke case records its exact expected exit and any essential output fields. Policies/input schemas follow the fixture files and module docstring; no private input is included.

Not a decoder, image optimizer, full PNG conformance validator or complete privacy guarantee. IDAT is not decompressed or validated; malicious pixel streams can survive. Unknown ancillary chunks and colour profiles remain and can contain identifying data. Pixel content itself may identify a person. APNG and unknown critical chunks are rejected. Some ancillary ordering/content constraints are not checked. 32 MiB, 10,000 chunks. A filesystem write failure can leave a partial new output; existing outputs are never overwritten.
