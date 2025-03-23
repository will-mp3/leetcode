"""
Given an integer array nums, 
return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0) # base case, guranteed sum of zero
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            # cant update set while we iterate through it, create dummy set nextDP
            nextDP = set()
            for t in dp:
                # check if target is found
                if (t + nums[i]) == target:
                    return True
                # add every value in dp and every value + nums[i] to nextDP
                nextDP.add(t)
                nextDP.add(t + nums[i])
            # update dp
            dp = nextDP
        
        return True if target in dp else False

"""
this solution turns what would normally be a brute force approach into a dynamic programming approach.
its important to first understand that we are looking for a sum that equals half the sum of the total array.
this implies two things, first if the array's sum is odd there is no solution.
second is that because the sums must be equal, if the target is found once its guranteed to be found again meaning there is a solution.
knowing this we can set up our solution first by checking the odd sum case.
next we can create our dp set and add zero as a base case.
we will use this set to hold every possible sum based on the values in nums.
for example, if nums was [2, 5] we would add values to our set in the following order: dp = { 0, 5, 2, 7 }.
we do this exact logic on a larger scale, iterating through each value in nums and adding it as well as all of its possible sums.
we use a dummy set to accomplish this as we are simultaneously iterating through our original dp set.
each iteration for every value in dp we add the current dp value and the current value plus our current value in nums to our dummy set.
what this is doing is copying our current dp values as well as creating all of the new ones.
the dummy dp values are then copied over to our original dp.
each iteration we also check if any of our values equal our target, if so return True.
if the loop executes and the target is not found we return False.
"""