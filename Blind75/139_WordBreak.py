"""
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and  s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

"""
to solve this problem we make use of bottom up dynamic programming.
we will use the value after the last index of our word as the base case and set it equal to true.
we iterate backwards through our string s and loop through our words with each iteration, check two conditions:
if there enough lenght in the string to match any of the words and do the words match.
if both of these conditions are met that index i is set to whatever the next index from the word is.
for example if we have the string "leetcode" with wordDict ["leet", "code"] and we checked code already, the index where c is should be true.
this allows for us to check if the rest of the string has been word broken by the time we get to checking leet at index 0.
another example, leetcodex, would return false at index 0 and 4 because once index 4 is checked, it sees that index 8 is false
and the string is invalid.
this solution runs in O(n^2) quadratic time.
"""