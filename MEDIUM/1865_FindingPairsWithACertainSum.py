"""
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
"""

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # arrays for modification
        self.nums1 = nums1
        self.nums2 = nums2

        # map for quick access to value & counts
        self.map = {}
        for num in self.nums2:
            self.map[num] = 1 + self.map.get(num, 0)

    def add(self, index: int, val: int) -> None:
        # get original element
        num = self.nums2[index]

        # update base array
        self.nums2[index] = self.nums2[index] + val

        # decrement count of old value, increment count of new value
        self.map[num] -= 1
        self.map[self.nums2[index]] = 1 + self.map.get(self.nums2[index], 0)
        
    def count(self, tot: int) -> int:
        count = 0

        # two sum
        for num in self.nums1:
            if tot - num in self.map:       
                count += self.map[tot - num]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

"""

"""