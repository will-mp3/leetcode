"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 

If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # countT contains how many of each character we need, window is how many we have
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0) # initialize count of t (string to search for)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) # adding/updating count for c

            # does this count satisfy?
            if c in countT and window[c] == countT[c]: # check that we have exactly the right amount of character c
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r] # update result
                    resLen = (r - l + 1) # update result length
                
                #pop from the left of our window to minimize
                window[s[l]] -= 1

                # check if we removed a value we need and if we dont have enough of it as a result
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

"""
this solution is pretty complex so I added comments to ease the pain lol, use them while you read this in the future.
like most substring problems we use a sliding window technique (sort of) to solve this problem.
in order to find any substring at all, we need to keep track of a few values.
namely, the characters and amount of which we need, the characters and amount of which we have, and of course the result and its length.
we also keep track of the amount of characters we have and need, using their equality as a sign we have a match.
the way the algorithm works to find a substring is as follows:
we first save the needed characters and amounts in our countT dictionary.
then we iterate through the list of characters, adding them to our dictionary and updating their count.
we check to see if this character is in countT and if the count is equal, if so we update our have value.
once/if have equals need, we check if our result length is less than the current result length, if so we update.
we then pop from our left value to start shrinking our list to check for smaller substrings.
we continue this process of updating and popping until have no longer equals need, we then proceed with the next character.
this continues until the entire array has been traversed, we then return our result.
this solution runs in O(n) linear time.
"""