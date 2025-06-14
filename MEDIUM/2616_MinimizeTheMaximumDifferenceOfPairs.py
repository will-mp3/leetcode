"""
You are given a 0-indexed integer array nums and an integer p. 
Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. 
Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, 
where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
"""

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count
        
        left, right = 0, nums[-1] - nums[0] # 0 and the max difference in the array
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left

"""
this problems solution relies on a modified binary search utilizing threshholds.
the first thing we must notice is thatwe have to sort our array to get the smallest pairs.
our differences will automatically be sorted as adjacents and we can move two indexes at a time to avoid repeat indices.
using our new list of numbers, we want to perform a binary search to find the smallest difference efficiently.
we are going to use a threshold for this rather than an index.
intuitively we could check al the pairs for diff = 1, diff = 2, etc and find our answer, albeit inneficient.
this diff value is our threshold, and we check each time if there is atleast p pairs meeting the threshhold.
to speed things up we use binary search, with our left and right set to 0 and the maximum difference respectively.
while left < right we get our middle value and calculate the value of pairs with a threshold of mid using a helper function.
if we have atleast p pairs, we check the left partition for a smaller threshold, if we have less than p check the right partition.
we return left when the binary search is complete, which will be set to the smallest threshold we found.
"""