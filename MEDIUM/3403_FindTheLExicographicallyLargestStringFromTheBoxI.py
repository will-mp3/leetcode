"""
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.
"""

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        curMax = ""
        
        # sliding window, repeatedly updating max with a window the min between:
        # (i + n - numFriends + 1), our max answer length formula
        # n, the length of word (for when we (i + n - numFriends + 1)is out of bounds)
        for i in range(n):
            curMax = max(curMax, word[i : min(i + n - numFriends + 1, n)])
        
        return curMax

"""

"""