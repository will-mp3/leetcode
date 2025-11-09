"""
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
"""

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            cnt = Counter(nums[i : i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)
        return ans

"""
This solution iterates through all possible k-length subarrays of the input array nums. For each subarray, it counts the occurrences of each element using a Counter. 
It then sorts the elements based on their frequency (and value in case of ties) and calculates the x-sum by summing the top x most frequent elements. 
The results are collected in a list and returned at the end.
The time complexity of this solution is O((n - k + 1) * (k + m log m)), where n is the length of nums, k is the length of the subarray, and m is the number of distinct elements in each subarray.
"""