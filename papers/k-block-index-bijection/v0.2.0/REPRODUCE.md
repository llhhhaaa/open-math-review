# Reproduce v0.2.0

## Finite Evidence

The included Python checker uses only the standard library.

```powershell
Set-Location evidence/code
python run_k_block_evidence.py --maximum-k 5 --maximum-total 25 --run-id local --output ../finite-certificate.local.json
```

The result should report `failure_count: 0`, `checked_partitions: 14248`, and
`checked_admissible_inverse_pairs: 58243`. This is finite computational
evidence, not a proof of the unbounded statement.

## PDF Build

Install a TeX distribution providing `latexmk`, BibTeX, and the `amsart`
class. From this version directory, run:

```powershell
./build.ps1
```

The script writes the derived PDF to `pdf/`. It never changes the manuscript
source.
