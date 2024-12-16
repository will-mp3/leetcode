"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # check if same value as before
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 # next lines update pointers once a solution is found, accountting for adjacent duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res

"""
the first thing to consider when solving this problem is the paramter that no duplicate triplets are allowed.
why this is considerable is because if there are duplicate values in the array you may see duplicate solutions.
consider the array [-3, 3, 4, -3, 1, 2], when parsing you will likely generate {-3, 1, 2} twice.
to remedy this we can sort the list so that duplicate values are next to each other and we can work around them.
this sorting also allows us to use pointers to later solve the problem.
if we work with the formula a + b + c = 0, we can use a left and right pointer to transform this into a + l + r = 0.
this will allow us to solve this problem by decreasing r when our result is greater than 0 
or increasing l when our result is less than 0 (possible due to the sorting).
"""