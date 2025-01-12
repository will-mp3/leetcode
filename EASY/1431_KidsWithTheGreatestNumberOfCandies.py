"""
There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 
denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)

        return res

"""
this problem is very straightforward.
to start, we need to find what the max candy value is since we will have to compare it later.
we initialize an empty result array and iterate through all of the values in our candies list.
for each value, we check if the value plus the extra candies value is greater than or equal to our max candies value.
if true, we append True to our result list.
if false, we append False to our result list.
we then return the boolean list.
this solution runs in O(n) linear time.
"""