# G4 Review: v0.2.0

## Scope

The authoritative LaTeX source was frozen in commit
`2a372920c46c908ff73a31dbb54d2f30291713f8`. This review covers the manuscript
source, the constructive inverse, G2 run `20260722T045354Z`, both bibliography
entries, the compiler log, extracted PDF text, and all five rendered pages.

## Mathematical Claim

The manuscript proves the identity announced in Section 7.2 of Wang and Zhang,
arXiv:2607.16690v1, by an explicit bijection. It does not claim discovery of the
identity or establish publication priority.

The proof is constructive rather than an exhaustive proof:

1. The forward map repeatedly applies a simultaneous block transfer and records
   the resulting block indices.
2. Lemma 3.2 gives a terminating deterministic inverse `sigma_w` for every
   admissible pair `(mu,w)`, not only for weights observed on sampled orbits.
3. Lemma 3.3 proves that each forward transfer satisfies the admissibility bound
   and is recovered by `sigma_w`.
4. Conjugation converts the transfer sequence into a `k`-strict partition, and
   the reverse recursion reconstructs the unique preimage.

## Proof Audit

- **Greedy interval lemma:** each greedy decomposition has cardinality equal to
  the maximum size of a subset with pairwise distances greater than `k`.
  Status: internally checked.
- **Admissible inverse count:** writing `b_k(mu)=ak+t` and `w mod k=r`, the
  cases `r>=t` and `r<t` give respectively `a` and `a+1` reverse blocks.
  Status: internally checked.
- **Mutual inversion:** promoted values occupy pairwise separated intervals;
  the top-down transfer therefore lowers exactly the promoted occurrence in
  every reverse block and removes the adjoined residue part. Status: internally
  checked.
- **Empty and terminal boundaries:** the proof now handles `q=0`, empty `mu`,
  the absence of a terminal block, and the two possible locations of the lowest
  block after transfer. Status: internally checked.
- **Forward recovery:** transformed nonterminal supports lie in the separated
  intervals `[c_j,c_j+k]`; the bottom-up algorithm recovers them in order.
  Status: internally checked.
- **Block-index drop:** the two formulas `ak+t` and `(a-1)k+t` give a difference
  in `{0,...,k-1}`. Status: internally checked.
- **Bijection:** the reverse recursion is defined for every conjugate of a
  `k`-strict partition and is unique by the one-step inverse. Status: internally
  checked.

No counterexample or unresolved internal step was found. This is not an
independent subject-matter review.

## Computational Support

G2 exhaustively checked 14,248 `k`-regular partitions for `2<=k<=5` and total
at most 25. It separately checked 58,243 admissible inverse pairs, including
the empty boundary, and found no failure. Independent product coefficients
matched through degree 25. These finite checks support the implementation; they
are not the proof of the unbounded theorem.

## Citations

- Every citation key used by the manuscript is present in `references.bib`, and
  neither bibliography entry is unused.
- Wang and Zhang title, authors, arXiv identifier, version, and 2026-07-18 date
  were checked against the arXiv API on 2026-07-22.
- Li, Wang, and Xu title, authors, journal, volume 173, article 102993, year 2026,
  and DOI `10.1016/j.aam.2025.102993` were checked against Crossref on
  2026-07-22.

## Build And Visual Review

- TeX Live 2026 `latexmk` and BibTeX completed successfully.
- The final log contains no LaTeX error, undefined citation, unresolved
  reference, overfull box, underfull box, or rerun warning.
- The PDF contains five nonblank letter-size pages with populated title,
  author, subject, and keyword metadata.
- All rendered pages were inspected at 180 dpi. The theorem, reverse algorithm,
  boundary cases, equations, example table, and bibliography are legible and
  remain within the page bounds. The example heading precedes its fixed table.

## Finding And Repair Log

- **G4-04, central proof:** v0.1.0 compressed the inverse-transfer argument and
  did not fully expose the constructive recovery. Replaced by a support-based
  greedy lemma, an explicit finite inverse, and a detailed mutual-inversion
  proof. Status: closed in v0.2.0.
- **G4-05, empty reverse decomposition:** the first v0.2.0 draft referred to
  `b_1` when the reverse-block count could be zero. The proof now handles
  `q=0` separately. Status: closed before source freeze.
- **G4-06, block identity wording:** an intermediate draft inferred equality of
  block decompositions from a lemma proving only equality of block counts. The
  source now uses the lemma only for cardinality and proves interval recovery
  separately. Status: closed before source freeze.
- **G4-07, float order:** the example table could precede its section heading.
  The final source fixes the table in place. Status: closed.
- **G4-08, independent proof review:** no external partition-theory specialist
  has reviewed the final proof. Status: open; blocks non-draft release.
- **G4-09, novelty:** the source paper announces the identity and leaves its proof
  to the reader; available searches do not establish priority for this explicit
  bijection. Status: open; blocks novelty claims and non-draft release.

## Verdict

The manuscript now contains an explicit constructive proof, with finite
computation used only as supporting evidence. The source, citations, build, and
rendered output pass this internal review. Delivery remains `draft_only` until
independent mathematical review and a fuller prior-art audit are completed.
