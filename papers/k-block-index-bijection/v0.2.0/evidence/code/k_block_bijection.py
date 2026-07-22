"""Exact k-block transfer map for the announced Wang--Zhang identity.

For a fixed integer k >= 2, this module implements the transfer map from
k-regular partitions to k-strict partitions described in Section 7.2 of
Wang--Zhang, arXiv:2607.16690v1.  It also contains a finite, exhaustive
certificate checker; that checker is evidence for the implementation and does
not replace the combinatorial proof.
"""

from __future__ import annotations

from collections import Counter, defaultdict


def _validate_k_regular(partition: tuple[int, ...], k: int) -> None:
    if k < 2:
        raise ValueError("k must be at least 2")
    if any(part <= 0 or part % k == 0 for part in partition):
        raise ValueError("a k-regular partition has positive parts not divisible by k")
    if any(left < right for left, right in zip(partition, partition[1:])):
        raise ValueError("a partition must be nonincreasing")


def _blocks_from_largest(partition: tuple[int, ...], k: int) -> list[tuple[int, int]]:
    """Return the (largest part, weight) pairs in the k-block decomposition."""
    _validate_k_regular(partition, k)
    values = sorted(set(partition), reverse=True)
    blocks: list[tuple[int, int]] = []
    index = 0
    while index < len(values):
        top = values[index]
        next_index = index + 1
        while next_index < len(values) and values[next_index] >= top - k:
            next_index += 1
        blocks.append((top, top if top <= k else k))
        index = next_index
    return blocks


def block_index(partition: tuple[int, ...], k: int) -> int:
    """Compute the k-block index b_k of a k-regular partition."""
    return sum(weight for _, weight in _blocks_from_largest(partition, k))


def tau(partition: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Move one largest part of each k-block down by k, simultaneously."""
    _validate_k_regular(partition, k)
    multiplicities = Counter(partition)
    for top, _ in _blocks_from_largest(partition, k):
        multiplicities[top] -= 1
        if multiplicities[top] == 0:
            del multiplicities[top]
        if top > k:
            multiplicities[top - k] += 1
    return tuple(
        part
        for part in sorted(multiplicities, reverse=True)
        for _ in range(multiplicities[part])
    )


def sigma(partition: tuple[int, ...], weight: int, k: int) -> tuple[int, ...]:
    """Invert one transfer step when ``weight`` is the prior k-block index."""
    _validate_k_regular(partition, k)
    if weight <= 0:
        raise ValueError("a k-block weight must be positive")

    multiplicities = Counter(partition)
    remainder = weight % k
    if remainder:
        multiplicities[remainder] += 1

    # Parts at most ``remainder`` belong to the exceptional bottom block.
    # Every remaining block is recovered from its smallest part upward.
    values = sorted(part for part in multiplicities if part > remainder)
    index = 0
    while index < len(values):
        bottom = values[index]
        next_index = index + 1
        while next_index < len(values) and values[next_index] <= bottom + k:
            next_index += 1
        multiplicities[bottom] -= 1
        if multiplicities[bottom] == 0:
            del multiplicities[bottom]
        multiplicities[bottom + k] += 1
        index = next_index

    return tuple(
        part
        for part in sorted(multiplicities, reverse=True)
        for _ in range(multiplicities[part])
    )


def transfer_sequence(partition: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Record the k-block indices along repeated transfer steps."""
    _validate_k_regular(partition, k)
    sequence: list[int] = []
    current = partition
    while current:
        sequence.append(block_index(current, k))
        current = tau(current, k)
    return tuple(sequence)


def conjugate(sequence: tuple[int, ...]) -> tuple[int, ...]:
    """Return the ordinary conjugate partition of a nonempty sequence."""
    if not sequence:
        return ()
    if any(value <= 0 for value in sequence):
        raise ValueError("a sequence must have positive entries")
    if any(left < right for left, right in zip(sequence, sequence[1:])):
        raise ValueError("a sequence must be nonincreasing")
    return tuple(
        sum(value >= level for value in sequence)
        for level in range(1, sequence[0] + 1)
    )


def transfer_map(partition: tuple[int, ...], k: int) -> tuple[int, ...]:
    """Map a k-regular partition to the conjugate of its transfer sequence."""
    return conjugate(transfer_sequence(partition, k))


def ell_k(partition: tuple[int, ...], k: int) -> int:
    """Compute the k-alternating length used in Wang--Zhang's identity."""
    if any(part <= 0 for part in partition):
        raise ValueError("a partition must have positive parts")
    if any(left < right for left, right in zip(partition, partition[1:])):
        raise ValueError("a partition must be nonincreasing")
    if any(count >= k for count in Counter(partition).values()):
        raise ValueError("ell_k is defined here for k-strict partitions")
    return sum(
        partition[start] - (partition[start + k - 1] if start + k - 1 < len(partition) else 0)
        for start in range(0, len(partition), k)
    )


def k_regular_partitions(total: int, k: int, maximum_part: int | None = None):
    """Yield all k-regular partitions of ``total`` in reverse lexicographic order."""
    if total < 0:
        raise ValueError("the partition total must be nonnegative")
    if k < 2:
        raise ValueError("k must be at least 2")
    if total == 0:
        yield ()
        return

    cap = total if maximum_part is None else min(total, maximum_part)
    for part in range(cap, 0, -1):
        if part % k:
            for suffix in k_regular_partitions(total - part, k, part):
                yield (part,) + suffix


def finite_certificate(maximum_k: int, maximum_total: int) -> dict[str, object]:
    """Exhaustively check the transfer-map invariants over a finite domain."""
    if maximum_k < 2 or maximum_total < 0:
        raise ValueError("maximum_k must be at least 2 and maximum_total nonnegative")

    checked = 0
    checked_admissible_inverse_pairs = 0
    failures: list[dict[str, object]] = []
    images: dict[tuple[int, int, tuple[int, ...]], tuple[int, ...]] = {}
    per_k: dict[str, int] = defaultdict(int)

    for k in range(2, maximum_k + 1):
        for weight in range(1, k):
            checked_admissible_inverse_pairs += 1
            reconstructed = sigma((), weight, k)
            if tau(reconstructed, k) != () or block_index(reconstructed, k) != weight:
                failures.append(
                    {
                        "reason": "sigma fails for an admissible inverse pair",
                        "k": k,
                        "partition": [],
                        "weight": weight,
                        "reconstructed": list(reconstructed),
                    }
                )
                return {
                    "maximum_k": maximum_k,
                    "maximum_total": maximum_total,
                    "checked_partitions": checked,
                    "checked_admissible_inverse_pairs": checked_admissible_inverse_pairs,
                    "checked_by_k": dict(per_k),
                    "failure_count": len(failures),
                    "failures": failures,
                    "all_checks_passed": False,
                }

        for total in range(1, maximum_total + 1):
            for partition in k_regular_partitions(total, k):
                checked += 1
                per_k[str(k)] += 1
                current_index = block_index(partition, k)
                for weight in range(current_index, current_index + k):
                    checked_admissible_inverse_pairs += 1
                    prior = sigma(partition, weight, k)
                    if tau(prior, k) != partition or block_index(prior, k) != weight:
                        failures.append(
                            {
                                "reason": "sigma fails for an admissible inverse pair",
                                "k": k,
                                "total": total,
                                "partition": list(partition),
                                "block_index": current_index,
                                "weight": weight,
                                "reconstructed": list(prior),
                            }
                        )
                        return {
                            "maximum_k": maximum_k,
                            "maximum_total": maximum_total,
                            "checked_partitions": checked,
                            "checked_admissible_inverse_pairs": checked_admissible_inverse_pairs,
                            "checked_by_k": dict(per_k),
                            "failure_count": len(failures),
                            "failures": failures,
                            "all_checks_passed": False,
                        }

                sequence = transfer_sequence(partition, k)
                image = conjugate(sequence)
                reconstructed: tuple[int, ...] = ()
                for weight in reversed(sequence):
                    reconstructed = sigma(reconstructed, weight, k)
                key = (k, total, image)
                collision = images.get(key)
                if collision is None:
                    images[key] = partition

                reason = None
                if any(not (0 <= left - right < k) for left, right in zip(sequence, sequence[1:])):
                    reason = "transfer sequence violates the k-gap bound"
                elif any(count >= k for count in Counter(image).values()):
                    reason = "conjugate image is not k-strict"
                elif reconstructed != partition:
                    reason = "sigma does not reconstruct the source partition"
                elif sum(image) != total:
                    reason = "the transfer map does not preserve size"
                elif len(image) != block_index(partition, k):
                    reason = "the transfer map does not preserve the block-index statistic"
                elif ell_k(image, k) != len(partition):
                    reason = "the transfer map does not preserve the length statistic"
                elif collision is not None and collision != partition:
                    reason = "two source partitions have the same image"

                if reason is not None:
                    failures.append(
                        {
                            "reason": reason,
                            "k": k,
                            "total": total,
                            "partition": list(partition),
                            "sequence": list(sequence),
                            "image": list(image),
                        }
                    )
                    return {
                        "maximum_k": maximum_k,
                        "maximum_total": maximum_total,
                        "checked_partitions": checked,
                        "checked_admissible_inverse_pairs": checked_admissible_inverse_pairs,
                        "checked_by_k": dict(per_k),
                        "failure_count": len(failures),
                        "failures": failures,
                        "all_checks_passed": False,
                    }

    return {
        "maximum_k": maximum_k,
        "maximum_total": maximum_total,
        "checked_partitions": checked,
        "checked_admissible_inverse_pairs": checked_admissible_inverse_pairs,
        "checked_by_k": dict(per_k),
        "failure_count": 0,
        "failures": [],
        "all_checks_passed": True,
    }


def independent_count_check(k: int, maximum_total: int) -> dict[str, object]:
    """Compare the two classical generating products without using the map."""
    if k < 2 or maximum_total < 0:
        raise ValueError("k must be at least 2 and maximum_total nonnegative")

    k_regular = [0] * (maximum_total + 1)
    k_regular[0] = 1
    for part in range(1, maximum_total + 1):
        if part % k:
            for total in range(part, maximum_total + 1):
                k_regular[total] += k_regular[total - part]

    k_strict = [0] * (maximum_total + 1)
    k_strict[0] = 1
    for part in range(1, maximum_total + 1):
        updated = k_strict.copy()
        for copies in range(1, k):
            offset = copies * part
            for total in range(offset, maximum_total + 1):
                updated[total] += k_strict[total - offset]
        k_strict = updated

    return {
        "k": k,
        "maximum_total": maximum_total,
        "k_regular_coefficients": k_regular,
        "k_strict_coefficients": k_strict,
        "matches": k_regular == k_strict,
    }
