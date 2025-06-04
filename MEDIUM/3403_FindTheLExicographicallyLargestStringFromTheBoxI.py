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
this solution uses a clever formula alongside a sliding window for its solution.
we are able to calculate the max length of our answer using the formula len(word) - numFriends + 1.
using this we can create a sliding window taking chunks of that size for every index in the word.
each time we check if the new window is larger than the one we have saved and update if necessary.
we also keep in mind the index and when necessary opt for the window to be from i to len(word) to stay in bounds.
this solution runs in O(n) linear time.
"""