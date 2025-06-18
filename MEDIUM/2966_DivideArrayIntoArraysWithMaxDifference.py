"""
You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.

Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:

The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. 
And if there are multiple answers, return any of them.
"""

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        subC = len(nums) // 3
        res = []
        sort = sorted(nums)
        
        cur = []
        for num in sort:
            cur.append(num) # add values to cur array
            if len(cur) == 3:
                # logic to check k difference
                if abs(cur[0] - cur[1]) > k or abs(cur[1] - cur[2]) > k or abs(cur[0] - cur[2]) > k:
                    return []

                res.append(cur)
                cur = []
        
        return res

"""

"""