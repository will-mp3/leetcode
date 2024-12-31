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
for this problem we make use of a hash map to keep track of our anagrams.
we start by initializing our result map, this is what will hold our anagrams.
next we go through each given string, for each string we map the count of its characters to an array and use it as a key.
to do this we create an array of length 26 and use ascii calculations to increment the correct indices based on character.
once this string identifying array is complete we use it as a key in our result array.
for example "cat" would have an array key of [1,0,1,.....,1] (final one is in the t index), a word like tac would share the same array key.
we add this key and its strings that correspond and return.
"""