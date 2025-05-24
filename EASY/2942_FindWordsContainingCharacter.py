"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res

"""
super simple solution here, no fancy algorithm.
we go throught the entire given array of words using a for loop to track the index.
each time we check if character x is in the word at index i, if so add index i to our result.
at the end return result
"""