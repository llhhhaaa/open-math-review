# Open Math Review

An open collection of GPT-generated mathematical manuscripts released for
scrutiny, correction, and reproducibility.

## Read This First

Every item is an **open-review-only draft** unless its own status file says
otherwise. Compilation, finite computation, and internal review do not certify
an unbounded mathematical argument. Do not cite an item here as an established
theorem, a peer-reviewed publication, or a claim of novelty.

All manuscript prose and research code in this repository were written by
GPT. Mechanical build artifacts were produced by the listed tools. No person,
institution, or affiliation is presented as a mathematical endorsement.

## Featured Draft

### An Explicit Bijection for the k-Block Index

- **Version:** `v0.2.0`
- **Status:** `open_review_only`
- **Direct PDF:** [download the release asset](https://github.com/llhhhaaa/open-math-review/releases/download/k-block-index-bijection-v0.2.0-open-review/k-block-index-bijection-v0.2.0-open-review.pdf)
- **Release record:** [k-block-index-bijection v0.2.0 open review](https://github.com/llhhhaaa/open-math-review/releases/tag/k-block-index-bijection-v0.2.0-open-review)
- **Technical index:** [paper README](papers/k-block-index-bijection/README.md)

The manuscript proposes a direct bijection from `k`-regular partitions to
`k`-strict partitions for every integer `k >= 2`. It is intended to preserve
partition size, send the `k`-block index to partition length, and send the
ordinary length to the `k`-alternating length. This is the identity stated in
Section 7.2 of Wang and Zhang's [arXiv:2607.16690v1](https://arxiv.org/abs/2607.16690v1).

The public evidence includes an explicit reverse construction and a finite
certificate with 14,248 checked `k`-regular partitions, 58,243 admissible
inverse pairs, and zero observed failures for `2 <= k <= 5` and total at most
25. These checks are evidence for the implementation, not a proof for all
partitions. Independent proof review and a sufficient prior-art review remain
open.

## Repository Map

| Location | Purpose |
| --- | --- |
| [`papers/k-block-index-bijection/v0.2.0/latex`](papers/k-block-index-bijection/v0.2.0/latex) | Authoritative editable LaTeX source. |
| [`papers/k-block-index-bijection/v0.2.0/pdf`](papers/k-block-index-bijection/v0.2.0/pdf) | Versioned PDF stored in the repository. |
| [`papers/k-block-index-bijection/v0.2.0/evidence`](papers/k-block-index-bijection/v0.2.0/evidence) | Finite certificate and standard-library Python checker. |
| [`papers/k-block-index-bijection/v0.2.0/REPRODUCE.md`](papers/k-block-index-bijection/v0.2.0/REPRODUCE.md) | Exact finite-check and PDF-build instructions. |
| [`papers/k-block-index-bijection/v0.2.0/STATUS.md`](papers/k-block-index-bijection/v0.2.0/STATUS.md) | What the version does and does not establish. |

## How To Review

Useful feedback identifies a falsifiable or verifiable claim. The main review
targets for the featured draft are the greedy interval lemma, the reverse
transfer, the mutual-inversion argument, boundary cases, and prior art.

- [Open a proof-check issue](https://github.com/llhhhaaa/open-math-review/issues/new/choose) for a specific theorem, lemma, equation, or implication.
- [Open a counterexample-or-bug issue](https://github.com/llhhhaaa/open-math-review/issues/new/choose) with `k`, a minimal partition or program input, and a reproduction.
- [Open a prior-art issue](https://github.com/llhhhaaa/open-math-review/issues/new/choose) with a DOI, arXiv identifier, or stable source and the exact overlap.

A correction is more valuable than a vague endorsement. See
[CONTRIBUTING.md](CONTRIBUTING.md) for versioning and attribution rules.

## Versioning And License

Each paper version is frozen in its own directory. The `latex/` directory is
the only editable manuscript source for that version; later repairs are
released as a new version rather than silently replacing an old one.

The prose and LaTeX sources are licensed under [CC BY 4.0](LICENSE). The
verification code is licensed under [MIT](LICENSE-CODE).
