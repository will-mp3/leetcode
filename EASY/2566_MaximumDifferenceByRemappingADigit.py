"""
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
"""

class Solution:
    def minMaxDifference(self, num: int) -> int:
        minS, maxS = str(num), str(num)

        # find digit to replace for max
        for x in maxS:
            if x != "9":
                maxRep = x
                break
            maxRep = "9"

        minS = minS.replace(maxS[0], "0")
        maxS = maxS.replace(maxRep, "9")

        return int(maxS) - int(minS)

"""
we take a greedy approach to this problem by analyzing two things:
the largest value can be made by flipping the most significant digit (that isnt already 9) to 9.
the smallest value can be made by flipping the most significant digit to 0.
knowing this we flip the first digit (and all its occurences) to 0 for our minimum value.
we then find our max value to flip by finding the first value that is not 9 and saving it.
we then flip every occurence of this value to 9 for our max value.
return the difference of the two strings.
"""