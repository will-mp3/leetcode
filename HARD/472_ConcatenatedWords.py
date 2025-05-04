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
this problem uses recursion to repeatedly partition and check words in a set.
the idea here is we have a set of words and want to check if any of them are made up of two or more of the words in said set.
we also use caching to optimize just a little bit but the logic is hardly dependent on it.
our dfs function does most of the heavy lifting, our code starts by going through each word in our list and running dfs on it.
what happens in our dfs function is the word gets broken into prefix and suffix portions for every position in the given word.
if our prefix and suffix are both in our wordset we know we have a concatenated word and can return true.
this is the case when our current word can be broken into two parts.
for the instance in which it is three or more words we have an or statement in that same conditional.
this second conditional checks if our prefix is in wordset AND dfs(suffix) returns true.
if the latter is true then we know our suffix can acutally be broken into multiple partitions, which is where the recursion comes.
every time one of the two conditionals executes we return true until the recrusive stack is popped and add the word to our result.
if those never activate we return false and move to the next word in our original loop.
"""