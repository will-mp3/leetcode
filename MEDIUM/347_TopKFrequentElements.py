"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # increments count of number in dictionary, if it dosent exist get adds 0

        for n, c in count.items():
            freq[c].append(n) # this value n occurs c number of times

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

"""
this problem asks that we return the k most frequent numbers in a list.
to accomplish this effeciently we use a variant of bubble sort.
instead of using indices to map our counts, index 1 maps to the count of the value 1 etc, we use a different layout (array may be unbounded).
our modified hashmap will instead use the indices as the count, and map an array of all the values that appear that many times.
for example, if the value 1 appears 3 times, map[3] will yield [1].
this way, we know our hashmap will only be the length of our input array.
the way our algorithm works is by intializes our count map and frequency array of arrays.
we start by counting the values in our list of numbers and updating those counts in our hashmap.
next, we go through the pairs in our hashmap and append all of the pairs in order of occurance.
we then iterate through this frequency list backwards, since the higher indices are more frequent, and append these values to result.
once the length of result reaches the value of k we return result.
this solution runs in O(n) linear time.
"""