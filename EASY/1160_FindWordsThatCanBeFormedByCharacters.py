"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        charMap = {}
        for c in chars:
            charMap[c] = 1 + charMap.get(c, 0)
        print(charMap.items())
        
        for word in words:
            dummyMap = charMap.copy()
            rem = len(word)
            for c in word:
                if c in dummyMap and dummyMap[c] > 0:
                    rem -= 1
                    dummyMap[c] -= 1
                    if rem == 0:
                        res += len(word)
                    
        return res

"""

"""