"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        strlen = len(needle)
        l, r = 0, strlen - 1

        while r < len(haystack):
            word = haystack[l:r+1]
            if word == needle:
                return l
            l += 1
            r += 1

        return -1

"""
this solution uses a sliding window technique to find the given word in the given string of words.
we do this by defining our window length, which is the length of the word we are searching for.
once found we can set up our pointers to define our window, starting at 0 and our length - 1.
while our right pointer is still inbounds we build our word based on the characters in our window.
if this word is equal to our target word, we return the left pointer as the first index its seen.
otherwise, we increment both pointers to shift our window by 1.
this loop continues until a match is found or the right pointer goes out of bounds, returning -1.
this solution runs in O(n) linear time.
"""