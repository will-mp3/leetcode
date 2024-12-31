"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mapping the character count of each string to list of anagrams
        res = {}

        # initialize our values for each letter to 0
        for s in strs:
            count = [0] * 26 # a .... z

            # get the count of each letter and assign it to its index
            for c in s:
                count[ord(c) - ord("a")] += 1 # ascii of current letter minus ascii of a to find index

            key = tuple(count) # tuple must be used

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
    
        return list(res.values())

"""

"""