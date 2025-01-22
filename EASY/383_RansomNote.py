"""
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        # use the collections import to map characters and their counts
        magazine_counts = collections.Counter(magazine)
        ransom_counts = collections.Counter(ransomNote)

        for char, count in ransom_counts.items():
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
            
        return True

"""

"""