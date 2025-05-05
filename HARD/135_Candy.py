"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings) # create candy array

        # first pass, left to right checking left neighbor
        for i in range(1, len(ratings)): # skip index 0, no left neighbor
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        # first pass, right to left checking right neigbor
        for i in range(len(ratings) - 2, -1, -1): # skip last index, no right neighbor
            if ratings[i + 1] < ratings[i]:
                arr[i] = max(arr[i + 1] + 1, arr[i]) # second pass, only increment if you need to

        res = sum(arr)
        return res

"""

"""