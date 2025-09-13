"""
You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
"""

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel, cons = defaultdict(int), defaultdict(int)
        for c in s:
            if c in 'aeiou':
                vowel[c] += 1
            else:
                cons[c] += 1
        res = 0
        if vowel.values():
             res += max(vowel.values())
        if cons.values(): 
            res += max(cons.values())
        return res

"""

"""