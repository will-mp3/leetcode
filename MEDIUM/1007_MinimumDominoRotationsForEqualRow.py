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

"""