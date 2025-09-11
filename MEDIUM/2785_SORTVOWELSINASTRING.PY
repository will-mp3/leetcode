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
This code defines a solution to sort the vowels in a given string while keeping the consonants in their original positions. The function `sortVowels` takes a string `s` as input and returns a new string `t` where all consonants remain in their original places, and the vowels are sorted in nondecreasing order of their ASCII values.
The approach used in this solution can be broken down into the following steps:
1. Define a list `VOWELS` containing all the vowels (both lowercase and uppercase).
2. Initialize an empty list `vowels` to store the vowels found in the input string and an empty list `res` to build the resulting string.
3. Iterate through each character `c` in the input string `s`. If `c` is a vowel (i.e., it is in the `VOWELS` list), append it to the `vowels` list and append a placeholder (underscore '_') to the `res` list. If `c` is a consonant, append it directly to the `res` list.
4. Sort the `vowels` list to arrange the vowels in nondecreasing order of their ASCII values.
5. Initialize a pointer `j` to track the position in the `vowels` list. Iterate through the `res` list, and whenever a placeholder ('_') is encountered, replace it with the next vowel from the sorted `vowels` list and increment the pointer `j`.
6. Finally, join the `res` list into a single string and return it.
The time complexity of this solution is O(n log n) due to the sorting step, where n is the number of vowels in the string. The space complexity is O(n) for storing the vowels and the resulting string.
"""