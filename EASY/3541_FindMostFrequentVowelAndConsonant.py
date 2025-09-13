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
This code defines a solution to find the sum of the maximum frequencies of vowels and consonants in a given string `s`. The function `maxFreqSum` takes a string `s` as input and returns an integer representing the sum of the highest frequency of any vowel and the highest frequency of any consonant in the string.
The approach used in this solution can be broken down into the following steps:
1. Initialize two dictionaries, `vowel` and `cons`, using `defaultdict(int)` to store the frequency of each vowel and consonant, respectively.
2. Iterate through each character `c` in the string `s`. If `c` is a vowel (i.e., it is in the string 'aeiou'), increment its count in the `vowel` dictionary. If `c` is a consonant, increment its count in the `cons` dictionary.
3. Initialize a variable `res` to 0, which will hold the final result.
4. Check if there are any vowels recorded in the `vowel` dictionary. If so, add the maximum frequency of any vowel (using `max(vowel.values())`) to `res`.
5. Check if there are any consonants recorded in the `cons` dictionary. If so, add the maximum frequency of any consonant (using `max(cons.values())`) to `res`.
6. Return the value of `res`, which now contains the sum of the maximum frequencies of vowels and consonants.
The time complexity of this solution is O(n), where n is the length of the string `s`, as it requires a single pass through the string to count the frequencies. The space complexity is O(1) since the size of the dictionaries is limited to the number of unique vowels (5) and consonants (21) in the English alphabet, which is constant.
"""