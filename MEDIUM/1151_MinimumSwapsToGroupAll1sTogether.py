"""
Given a binary array data, 
return the minimum number of swaps required to group all 1's present in the array together in any place in the array.
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        l, r = 0, 0
        maxOnes = countOnes = 0

        while (r < len(data)):
            countOnes += data[r]
            r += 1

            if (r - l) > ones:
                countOnes -= data[l]
                l += 1

            maxOnes = max(maxOnes, countOnes)

        return ones - maxOnes

"""

"""