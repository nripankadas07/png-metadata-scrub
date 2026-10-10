# Research and candidate brief — 10 October 2026

User: Asset handoff reviewers removing specific text, EXIF and time chunks while preserving the encoded image stream.

Pain: An image optimizer can reencode pixels or remove display metadata. A review needs an exact account of which metadata was removed and a refusal to overwrite an existing file.

Smallest useful capability: Validate bounded PNG chunk framing/CRCs and key structural ordering, remove tEXt/zTXt/iTXt/eXIf/tIME, retain every other encoded chunk byte-for-byte, and write only to a new output path.

Demand is **inferred** from the workflow and established alternatives, not a verified request for this project. No invented users, adoption or growth promise.

Queries: `png optimizer sort:stars`, GitHub repository search with stars qualifier, bounded first five results plus named relevant established comparables. Connector coverage and relevance selection are limited; this is not an exhaustive ranking. Highest-star relevant comparable **among those inspected**: [kornelski/pngquant](https://github.com/kornelski/pngquant) (5754 stars). Stars are research context, not technical performance.

| Exact comparable | Observed stars | Last push UTC | API license metadata |
| --- | ---: | --- | --- |
| [oxipng/oxipng](https://github.com/oxipng/oxipng) | 4262 | 2026-10-06T22:22:31Z | MIT |
| [kornelski/pngquant](https://github.com/kornelski/pngquant) | 5754 | 2026-06-21T02:27:23Z | NOASSERTION |
| [google/zopfli](https://github.com/google/zopfli) | 3596 | 2026-09-30T13:34:47Z | Apache-2.0 |

Observed 10 October 2026 via GitHub repository metadata, current README and first five open issues. Missing README/license metadata is unavailable rather than evidence of absent support; NOASSERTION requires manual license review before any reuse. No reuse occurred. Archived status is preserved in raw research evidence; grafov/m3u8's README identifies its successor and suspended support.

Fair comparison: established alternatives have broader parsing, client, GUI, optimization, binding or management workflows and should be considered first. This tool offers the bounded offline workflow in the capability above, a Python source installation, synthetic example and exact failure exits. Its zero runtime dependencies do not establish better reliability or support. Installation and time-to-first-result were measured only for our examples; competitor installations and equivalent workloads were not benchmarked. We make no absence or superiority claim. Compare the stated scope/limitations with each alternative's current docs before selecting it.

Portfolio differentiation: photoflow organizes photo workflows; this changes a narrowly specified PNG metadata set with exact retained-byte evidence. The other four daily projects use different data, algorithms and users (video windows, mail graphs, SQL plans, PNG bytes, numeric ACLs); they are not subdivisions of one product.

Acceptance: the documented example produces its expected evidence; meaningful malformed inputs fail; original core behavior/regressions pass 14 tests; installed console command works outside source; remote CI runs Python 3.10, 3.12 and 3.14. Public existence without these checks is not a verified launch.

Discovery: png and metadata topics; a red-pixel synthetic example and deterministic removal receipt.

Limits: Not a decoder, image optimizer, full PNG conformance validator or complete privacy guarantee. IDAT is not decompressed or validated; malicious pixel streams can survive. Unknown ancillary chunks and colour profiles remain and can contain identifying data. Pixel content itself may identify a person. APNG and unknown critical chunks are rejected. Some ancillary ordering/content constraints are not checked. 32 MiB, 10,000 chunks. A filesystem write failure can leave a partial new output; existing outputs are never overwritten.

## Workflow comparison

Oxipng is a Rust lossless PNG optimizer with compression/filter and metadata options. pngquant converts images into palette PNGs, a different compression/image transformation workflow. Zopfli includes a PNG optimization tool using its compression implementation. Established tools should be considered for optimization or broader stripping policies. This MVP removes only five named metadata types and keeps all other bytes, with no IDAT decoding or reencoding. It is not a substitute for full image validation or comprehensive privacy scrubbing. API NOASSERTION licensing metadata was not interpreted as permission to reuse code. No competitor implementation was reused or timed.

Evidence observed between 06:12 and 06:22 UTC, 10 October 2026. Repository metadata is a snapshot; push time is activity evidence, not a support guarantee.
