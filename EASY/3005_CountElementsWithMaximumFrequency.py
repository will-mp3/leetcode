"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        maxC = 0

        for num in nums:
            counts[num] += 1
            maxC = max(maxC, counts[num])
        
        res = 0
        for count in counts.values():
            if count == maxC:
                res += count

        return res

"""
This code defines a solution to find the total frequencies of elements in an array that have the maximum frequency. The function `maxFrequencyElements` takes a list of positive integers `nums` as input and returns an integer representing the sum of the frequencies of the elements that occur most frequently in the array.
The approach used in this solution can be broken down into the following steps:
1. Initialize a dictionary `counts` using `defaultdict(int)` to store the frequency of each element in the array. Also, initialize a variable `maxC` to keep track of the maximum frequency encountered.
2. Iterate through each number `num` in the input list `nums`. For each number, increment its count in the `counts` dictionary and update `maxC` if the current count exceeds the previous maximum frequency.
3. Initialize a variable `res` to 0, which will hold the final result.
4. Iterate through the values in the `counts` dictionary. For each count, if it equals `maxC`, add it to `res`.
5. Return the value of `res`, which now contains the total frequencies of the elements with the maximum frequency.
The time complexity of this solution is O(n), where n is the length of the input list `nums`, as it requires a single pass through the list to count the frequencies and another pass through the counts to sum the maximum frequencies. The space complexity is O(k), where k is the number of unique elements in the array, due to the storage of the `counts` dictionary.
"""