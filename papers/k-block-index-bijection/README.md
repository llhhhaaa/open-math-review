# An Explicit Bijection for the k-Block Index

## Open-Review Status

- **Version:** `v0.2.0`
- **Status:** `open_review_only`
- **Independent proof review:** incomplete
- **Novelty and priority review:** unresolved

This is a GPT-generated manuscript released to invite falsification and
technical criticism. It is not peer reviewed and must not be presented as an
established theorem or a claim of priority.

The manuscript gives a candidate explicit bijection for an identity announced
by Wang and Zhang. The public version contains a constructive inverse and a
finite verification program. The finite tests support the implementation; they
do not replace a proof for arbitrary `k` and unbounded partitions.

## Review Focus

1. Check that the greedy interval lemma is sufficient for the claimed block
   recovery.
2. Check that the inverse transfer is well-defined in every residue and empty
   boundary case.
3. Check mutual inversion, size preservation, and both statistic
   correspondences.
4. Report an earlier explicit proof or a source that changes the priority
   boundary.

Open a focused proof-check, counterexample-or-bug, or prior-art issue using
the templates supplied in the repository.

## Contents

- [`v0.2.0/latex`](v0.2.0/latex): authoritative editable manuscript source.
- [`v0.2.0/pdf`](v0.2.0/pdf): PDF derived from that source.
- [`v0.2.0/evidence`](v0.2.0/evidence): finite certificate and exact Python
  checker.
- [`v0.2.0/review`](v0.2.0/review): internal review record, explicitly not an
  independent expert review.
- [`v0.2.0/STATUS.md`](v0.2.0/STATUS.md): release boundary and verification
  summary.
