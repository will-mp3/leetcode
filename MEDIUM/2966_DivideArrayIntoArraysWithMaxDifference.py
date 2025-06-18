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
this solution is rather simple and avoids the use of any tricky algorithm through pattern recognition.
we know that we are working with differences, and specifically with difference threshholds.
logically we choose to sort our array of numbers to minimize the difference ebtween adjacent elements.
this allows us to split our array nums in sub arrays with the most optimal grouping without any work.
knowing this we have a loop through our now sorted array.
the basic idea is we keep a cur array that appends itself to our our res array when it reaches three elements.
we use cur to repeatedly transfer an array of length three, effectively dividing the original array nums.
while this is happening we also check a condition when we reach length three, that being that the difference of all elements is <= k.
we use absolute value to save ourselves from doubling our required calculations and return an empty array if invalid.
this solution runs in O(n) linear time.
"""