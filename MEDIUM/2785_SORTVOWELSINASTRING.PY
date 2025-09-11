"""
Given a 0-indexed string s, permute s to get a new string t such that:

All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.
"""

class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowels = []
        res = []

        for c in s:
            if c in VOWELS:
                vowels.append(c)
                res.append('_')
            else:
                res.append(c)
        
        vowels.sort()
        
        j = 0
        if vowels:
            for i in range(len(res)):
                if j == len(vowels):
                    break
                
                if res[i] == '_':
                    res[i] = vowels[j]
                    j += 1

        return "".join(res)

"""

"""