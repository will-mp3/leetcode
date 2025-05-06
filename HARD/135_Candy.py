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
            if ratings[i - 1] < ratings[i]: # if i is greater than left neighbor
                arr[i] = arr[i - 1] + 1

        # first pass, right to left checking right neigbor
        for i in range(len(ratings) - 2, -1, -1): # skip last index, no right neighbor
            if ratings[i + 1] < ratings[i]:
                arr[i] = max(arr[i + 1] + 1, arr[i]) # second pass, only increment if you need to

        res = sum(arr)
        return res

"""
this solution dosent rely on any fancy algorithm, the key is being able to visualize the array and its patterns.
we know that we will need to analyze both neighbors to accurately decide whether to increase the candy count.
we will have to check both the amount of candy the neighbors have and their rank.
if we searched left to right in sorted order, we see this is extremely easy, the candies simply follow ascending order.
the same goes if we do right to left in reverse sorted order.
the same cannot be said for the standard case where the ranks are mixed.
to account for this we will search left to right, and only check the left neighbor.
this allows us to add candies without having to worry about future larger values.
if the left neighbor is larger we add 1 to the left neighbors cantdy count and store it at index i.
we then search right to left, checking the right neighbor this time.
this time we store the max of the right neighbors candy + 1 and the current count.
try drawing this out, it will make clearer sense.
"""