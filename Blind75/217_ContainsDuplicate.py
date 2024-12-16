class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hSet = set()

        for n in nums:
            if n in hSet:
                return True
            hSet.add(n)
        return False