# G2 Reproduction Report: 20260722T045354Z

## Scope

This run checks the exact implementation of the explicit block transfer and
its inverse over a finite domain. It is supporting evidence for the manuscript
proof, not a replacement for the all-`k` combinatorial argument.

## Command

```powershell
python research\candidate-02\g2-evidence\run_k_block_evidence.py `
  --maximum-k 5 `
  --maximum-total 25 `
  --run-id 20260722T045354Z `
  --output research\candidate-02\g2-evidence\runs\20260722T045354Z\finite-certificate.json
```

The command ran under system Python 3.12.10 on Windows 11. The exact platform
string, command line, and source hashes are recorded in the JSON certificate.

## Results

- Exhaustively checked 14,248 `k`-regular partitions for `2 <= k <= 5` and
  total at most 25.
- Exhaustively checked 58,243 admissible inverse pairs `(mu,w)`, including the
  empty-partition boundary, and verified both
  `tau(sigma_w(mu)) = mu` and `b_k(sigma_w(mu)) = w`.
- Found no collision, failed reconstruction, statistic mismatch, or violation
  of the transfer-sequence gap bound.
- Independently matched the ordinary generating-function coefficients for
  `k`-regular and `k`-strict partitions through degree 25 for every
  `2 <= k <= 5`.

The certificate verdict is `pass`. Its SHA-256 digest is
`3c7abcd94edfda7b4096c94fb4866e5554fea79318ff204bf055b1c577dd6073`
(hexadecimal digest, case-insensitive).

## Boundary

The finite run detects implementation errors and exercises the constructive
inverse beyond values arising on sampled forward orbits. The theorem for every
integer `k >= 2` and partitions of unbounded size is established, if correct,
by the manuscript's explicit inverse and proof of mutual inversion. Independent
subject-matter review remains a separate release requirement.
