# Open Math Review

An open collection of GPT-generated mathematical manuscripts released for
scrutiny, correction, and reproducibility.

## Status First

Every manuscript in this repository is an **open-review-only draft** unless
its own status file says otherwise. A successful build, an exhaustive finite
test, or an internal review is not an independent proof check. Do not cite an
item here as an established theorem, a peer-reviewed publication, or a claim
of novelty.

All manuscript prose and research code in this repository were written by
GPT. Mechanical build artifacts were produced by the listed tools. No person,
institution, or affiliation is presented as a mathematical endorsement.

## Current Papers

| Paper | Version | Status | Review request |
| --- | --- | --- | --- |
| [An Explicit Bijection for the k-Block Index](papers/k-block-index-bijection/README.md) | `v0.2.0` | `open_review_only` | Check the constructive inverse, boundary cases, and prior art. |

## How To Contribute

Useful feedback is specific and reproducible. Please use one of these issue
types:

- **Proof check:** identify the exact statement, step, and justification that
  should be checked.
- **Counterexample or bug:** give the parameter values, input, observed output,
  and a minimal reproduction where possible.
- **Prior art:** give a stable URL, DOI, or arXiv identifier and state precisely
  which claim it overlaps.

The repository welcomes criticism. A correction is more valuable than a vague
endorsement. Proposed changes should preserve the paper versioning rules in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Release Model

Each paper version is frozen in its own directory. The `latex/` directory is
the authoritative editable source for that version; the PDF and evidence are
derived artifacts. Later changes are released as a new version, never by
silently replacing a prior one.

The prose and LaTeX sources are licensed under [CC BY 4.0](LICENSE). The
verification code is licensed under [MIT](LICENSE-CODE).
