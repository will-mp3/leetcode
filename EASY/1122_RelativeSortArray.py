"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {}
        
        for num in arr1:
            if num in map:  
                map[num] += [num]
            else:
                map[num] = [num]
        
        copy = []
        
        for num in arr2:
            copy = copy + map[num]
        
        for num in sorted(arr1):
            if num not in arr2:
                copy = copy + [num]
        
        arr1 = copy
        return arr1