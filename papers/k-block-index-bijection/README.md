# An Explicit Bijection for the k-Block Index

## Quick Links

- **PDF:** [direct download](https://github.com/llhhhaaa/open-math-review/releases/download/k-block-index-bijection-v0.2.0-open-review/k-block-index-bijection-v0.2.0-open-review.pdf)
- **Release:** [v0.2.0 open-review record](https://github.com/llhhhaaa/open-math-review/releases/tag/k-block-index-bijection-v0.2.0-open-review)
- **Source:** [`v0.2.0/latex`](v0.2.0/latex)
- **Finite evidence:** [`v0.2.0/evidence`](v0.2.0/evidence)
- **Reproduction:** [`v0.2.0/REPRODUCE.md`](v0.2.0/REPRODUCE.md)
- **Feedback:** [open an issue](https://github.com/llhhhaaa/open-math-review/issues/new/choose)

## Status

- **Version:** `v0.2.0`
- **Status:** `open_review_only`
- **Independent proof review:** incomplete
- **Novelty and priority review:** unresolved

This is a GPT-generated manuscript released to invite falsification and
technical criticism. It is not peer reviewed and must not be presented as an
established theorem or a claim of priority.

## Candidate Result

For every integer `k >= 2`, the manuscript proposes a bijection
`Phi_k : R_k -> S_k`, where `R_k` is the set of `k`-regular partitions and
`S_k` is the set of `k`-strict partitions. For a proposed image `Phi_k(lambda)`,
the intended identities are:

```text
|Phi_k(lambda)| = |lambda|
length(Phi_k(lambda)) = k-block-index(lambda)
k-alternating-length(Phi_k(lambda)) = length(lambda)
```

The identity was stated, with its proof left to the reader, in Section 7.2 of
Wang and Zhang, [Euler's partition theorem and lecture hall partition theorem](https://arxiv.org/abs/2607.16690v1).
The manuscript gives a candidate direct construction: repeatedly apply a
simultaneous block transfer, conjugate the resulting block-index sequence, and
recover the preimage by an explicit bottom-up reverse transfer.

## Verification Boundary

The finite checker verifies the implementation over all `k`-regular partitions
with `2 <= k <= 5` and total at most 25. It checked 14,248 source partitions
and 58,243 admissible inverse pairs, with zero failures. It also compares the
two generating-product coefficient sequences through degree 25.

This is supporting evidence only. It does not prove the claim for arbitrary
`k` or unbounded partitions. Independent proof review and novelty/priority
review remain unresolved.

## Review Focus

| Location | Question for reviewers |
| --- | --- |
| Lemma 3.1 | Does the greedy interval lemma give exactly the needed block-count recovery? |
| Lemma 3.2 | Is the reverse transfer well-defined for every residue and empty boundary case? |
| Lemma 3.3 | Does the forward transfer satisfy the admissibility bound and recover under the reverse algorithm? |
| Theorem 2.1 and Section 4 | Do the recursive inverse, size preservation, and both statistic identities follow globally? |
| Literature | Is there an earlier explicit bijection or result that changes the priority boundary? |

Use the issue templates for a focused proof check, counterexample, implementation
bug, or prior-art correction. Quote a theorem, lemma, equation, or code path;
do not ask the community to referee the entire manuscript without a specific
claim to test.

## Contents

- [`v0.2.0/latex`](v0.2.0/latex): authoritative editable manuscript source.
- [`v0.2.0/pdf`](v0.2.0/pdf): PDF derived from that source.
- [`v0.2.0/evidence`](v0.2.0/evidence): finite certificate and exact Python
  checker.
- [`v0.2.0/review`](v0.2.0/review): internal review record, explicitly not an
  independent expert review.
- [`v0.2.0/STATUS.md`](v0.2.0/STATUS.md): release boundary and verification
  summary.
