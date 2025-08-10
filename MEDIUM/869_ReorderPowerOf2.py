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
This code defines a solution to check if the digits of a given integer n can be reordered to form a power of two.
The `reorderedPowerOf2` method generates all possible permutations of the digits of n and checks if any of these permutations can form a power of two. 
It uses the `permutations` function from the `itertools` module to generate all combinations of the digits.
For each permutation, it converts the tuple of characters back to an integer and checks if it is a power of two by counting the number of '1's in its binary representation. 
If any permutation results in a valid power of two, the method returns True; otherwise, it returns False.
The time complexity of this solution is O(n!), where n is the number of digits in n, due to the generation of permutations, which can be computationally expensive for larger numbers.
"""