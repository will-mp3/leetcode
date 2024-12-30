"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

"""
this solution makes use of a sliding window.
the way this works is we initialize a left and right pointer, the left starts at 0 and the right continuously increments.
as the right pointer goes through the list, if the character is unique we add it to our charSet and calculate a new result.
once a duplicate character is found in our set, we remove the character at the left pointer and increment it, shrinking the window.
as these two results ebb and flow we continue to update our result with the max between the current result and size of current window.
once the loop completes we return our result.
this solution runs in O(n) linear time.
"""