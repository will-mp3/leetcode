"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # solve using recursion
        # base case
        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0) # pop the value at the 0 index and save it to n
            perms = self.permute(nums)

            # once the call stack starts returning, begin appending the popped value n
            for perm in perms:
                perm.append(n)
            
            # add all of the elements to result
            result.extend(perms)
            
            # add the removed element back
            nums.append(n)
        
        return result

"""
to solve this problem we use a recursive decision tree approach.
the top of our tree contains the original array nums.
we recursively explore the permutations by removing the first value and carrying the remaining array to the next level.
the value we pop is saved to n and will ultimately be appended once the call stack returns.
for example, if nums = [1, 2, 3] then the left-most child would be [2, 3] and that childs left-most child would be [3].
once we get to our base case len(nums) == 1, we pop our call stack and append all of those n values.
what that looks like with our example is [3] gets 2 appended and then 1 appended and returns [3, 2, 1] as a permutation.
"""