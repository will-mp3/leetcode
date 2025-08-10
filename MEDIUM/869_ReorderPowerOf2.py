"""
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.
"""

from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        string = str(n)
        arr = list(string)
        leng = len(string)

        for combo in permutations(arr, leng):
            num = int("".join(combo))

            if len(str(num)) != leng:
                continue

            if str(bin(num)).count('1') == 1:
                return True

        return False

"""

"""