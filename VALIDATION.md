# Validation — 10 October 2026

Acceptance suite: 14 meaningful core tests, module compilation, synthetic demo, wheel build and new-venv console commands outside source. Run `python verify.py`. No competitor benchmark was performed.

Remote CI is required before LIVE; receipts are recorded in the owner's chronological index. Supported matrix: Ubuntu/Python 3.10, 3.12, 3.14. Other OS/architectures are untested. Build tools must be available to run verification; the normal install path uses pip build isolation.

Not a decoder, image optimizer, full PNG conformance validator or complete privacy guarantee. IDAT is not decompressed or validated; malicious pixel streams can survive. Unknown ancillary chunks and colour profiles remain and can contain identifying data. Pixel content itself may identify a person. APNG and unknown critical chunks are rejected. Some ancillary ordering/content constraints are not checked. 32 MiB, 10,000 chunks. A filesystem write failure can leave a partial new output; existing outputs are never overwritten.

Local observed result: all acceptance checks passed on Linux/Python 3.12 with setuptools 84.0.0 and wheel 0.48.0. A new wheel environment, outside-source CLI success/failure checks and the synthetic demo passed. Remote matrix and normal build-isolated installation must still be verified at the public final commit.
