"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) 
in the given array.
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        # caching
        dp = {}

        def dfs(word):
            # if we have seen the word, return the value stored at it
            if word in dp:
                return dp[word]

            for i in range(1, len(word)): # dont want an empty prefix
                # break word into prefix and suffix
                prefix = word[:i]
                suffix = word[i:]

                # if both portions are in our wordset OR if the suffix has portions in the wordset
                if ((prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix))):
                    # if word passes the condition, set it to True in our cache
                    dp[word] = True
                    return dp[word]
                
            # if it dosent pass our conditional set it to False in our cache
            dp[word] = False
            return dp[word]

        res = [] # list of concatenated words
        for w in words: # check for every word
            if dfs(w):
                res.append(w)

        return res

"""

"""