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
for this solution we use two hashmaps to track the occurances of characters in both the magazine and ransom note for comparison.
we make use of the collections library here, alternatively we would make two dictinaries and track the occurances of each character.
once our two dictionaries are made, we iterate through the char and counts in randsom count.
for each character in ransom count, we assign magazine_count to the count for that character in our magazine_counts dictionary.
we then compare this magazine count to the current count and return false if its less than the count from ransom count.
if this loop executes without returning false, we know we can construct the ransom note and return true.
this solution runs in O(n) linear time.
"""