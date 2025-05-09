"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
If it cannot be done, return -1.
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # common value amoungst all dominoes must be one of the first two values
        for target in [tops[0], bottoms[0]]: # go through both target values
            # counts for missing targets on the top or bottom
            missingT, missingB = 0, 0

            # this allows us to iterate through both lists at once, we get each value in a pair
            for i, pair in enumerate(zip(tops, bottoms)):
                # extract values from the pair
                top, bottom = pair

                # if we find a set that dosent contain either target break and return -1
                if not (top == target or bottom == target):
                    break
                # if top is not our target increment the missing top value
                if top != target: missingT += 1
                # if bottom is not our target increment the missing bottom value
                if bottom != target: missingB += 1
                # once we get to the end return the minimum of the missing values
                if i == len(tops) - 1:
                    return min(missingT, missingB)

        return -1

"""
to solve this problem we know that if theres a solution then there is one value that every pair of dominoes has in common.
instead of checking all values one through six we can check the two values in the first set, since we know it must be one of those two.
the basic algorithm is we are looping through the top and bottom dominoes, and each time keeping track of the missing values in top and bottom.
if the target value is not present in the top, we increment missing top by one and vice versa.
at the end we return the minimum missing value from top or bottom.
the way the code works is by looping through once for each target value (twice total).
each time we track our missing top and missing bottom.
for each target we loop through each set of dominoes, which we get through a pair using the zip function.
if at any point we get a pair that dosent have the current target value, we break the loop and either return zero or check the next target.
if the current target is in our set we check if its misisng from the top or the bottom and increment.
if either target reaches the end of the list of dominoes we know our solution is present, a common value was found.
at this point we return the current minimum missing value.
this solution runs in O(n) linear time.
"""