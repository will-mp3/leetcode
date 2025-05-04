"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # optimization for duplicates
        wordDict = set(wordDict)

        # backtracking solution
        def backtrack(i):
            # reached end of the string
            if i == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                w = s[i:j+1] # build our word from index i to j
                if w in wordDict: # if our built word is in our list of words
                    cur.append(w)
                    backtrack(j + 1) # runs until we reach end of string, then adds all cur words
                    cur.pop() # once recursive stack pops clear cur word list and start next sentence

        cur = [] # words we have added so far
        res = []
        backtrack(0) # start at index 0
        return res

"""

"""