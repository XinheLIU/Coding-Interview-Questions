class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        We will compute \text{last[d] = i}last[d] = i, the index \text{i}i of the last occurrence of digit \text{d}d        (if it exists).

        Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will           swap it with the largest such digit; if there are multiple such digits, we will swap it with the one that           occurs the latest.
        """
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, -1) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num