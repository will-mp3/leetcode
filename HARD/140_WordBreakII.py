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
this solution makes use of backtracking to repeatedly search through our input string and build words & sentences.
we track a few variables in this problem, namely a cur list holding out current words and a result list with our sentences to be returned.
our backtracking function first checks our basecase, which is when we reach the end of our input string.
when this happens we join and append our current list of words to our result list.
the main logic takes us through all the characters past index i, which is a passed in parameter.
each iteration we build a new word to be checked with our word list.
if the word is present we add it to our current list and call our backtracking function from the next character after our word (j + 1).
this continues until our base case is found and our recursive stack pops, at this point we start removing words from our current list.
this recursion allows us to branch when a word, like cat, is found but still be able to check the next characters for a word, like cats.
ultimately the recursive stack pops through and we return out list of sentences.
"""