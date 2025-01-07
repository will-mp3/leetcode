"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 2, O(1) space complexity assuming sorting algorithms are considered negligible
        # return sorted(s) == sorted(t)

        # solution 3, kinda cheating
        # return Counter(s) == Counter(t)

        # solution 1, what you would typically submit
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        # build hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # iterate through hashmaps
        for c in countS:
            if countS[c] != countT.get(c, 0): # use get function to avoid key error if c dosent exist in countC
                return False
        return True

"""
this problem we are tasked with identifying anagrams, or more simply checking if strings contain identical characters.
above are three solutions, solution 2 sorts the strings alphabetically and compares if they are equal, meh.
solution 3 using a built in function thats main purpose is comparing characters, wouldnt recommend for an interview.
solution 1 is what I would recommend submitting, it makes use of two hashmaps to track character counts.
we start by ensuring the strings are the same length, if they arent return false.
we create and build two hashmaps by iterating through our strings and updating the counts of each character as we cross them.
once our hashmaps are built, we iterate once more to ensure the characters and counts are equal.
if at any point they are not equal return false, if our loop runs through completely return true.
this solution runs in O(n) linear time.
"""