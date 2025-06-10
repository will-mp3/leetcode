"""
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.
"""

class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd, minEven = 0, float('inf')
        map = {}

        for char in s:
            map[char] = 1 + map.get(char, 0)
        
        for val in map.values():
            if val % 2 == 0:
                minEven = min(minEven, val)
            else:
                maxOdd = max(maxOdd, val)

        return maxOdd - minEven

"""
this solution makes use of a hashmap to track the occurences of each character in s.
you could also use the collections library, but this is more general.
we count every time a character appears, each time incrementing its count in map.
once done we go through each value in our map and check if its even or odd.
we want to find the smallest even value and the largest odd value.
for each value, after we check even or odd, we check if its smaller or larger respectively.
once done we return the difference between our max oodd and min even values.
"""