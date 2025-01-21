"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # solution for O(n) time, O(n) space
        n = len(nums)
        a = [0] * n # initialize empty array

        for i in range(n):
            a[(i + k) % n] = nums[i] # use modular indexing since we are rotating cyclically

        nums[:] = a

        # solution for O(1) space, O(n * k) time
        n = len(nums)
        k %= n # for when k is greater than len(nums), saves us from O(n^2)

        for i in range(k):
            tmp = nums[-1]
            for j in range(n):
                nums[j], tmp = tmp, nums[j]

"""
for this problem I have provided two solutions based on priority, one aimed at time efficiency and one aimed at space efficiency
the first solution prioritizes time complexity, see comments for specifics.
the way it works is by using a separate array for data storage, we start by initializing an empty array of len(nums).
next, we iterate n times (length of nums), each time using modular indexing to sort our values in nums into our new array.
we know that we are shifting k times, so we start by adding k to current index i.
for values that exceed the length and move to the beggining we add a mod operation using the length of nums.
for each of these calculated indicies we save the value at indix i.
once finished we copy the contents of a into nums since we are asked to modify the existing array.
the second solution uses constant space but runs a little bit slower.
we start by saving our length in n like before, this time using n to mod our k value too avoid O(n^2) complexity.
we then iterate k times, more specifically we will rotate every element k times.
for each iteration we set our temp variable to the last value in nums, then we iterate though nums.
each iteration we set our current index to our temp variable and our tmp variable to our current index.
this line is particular because if separate into two operation the tmp variable will be altered and the algorithm will not work.
what this is doing simply put is setting the value before our current index to our current index while simultaneously saving the current index.
the current index we just saved becomes our previous value the next iteration, the above process executes again.
"""