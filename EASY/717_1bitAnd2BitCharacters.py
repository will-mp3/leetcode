"""
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
"""

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
          # see 0, move one space; see 1, move two space
            i += bits[i] + 1
        # check if we landed at the last bit or skipped it
        return i == n - 1

"""
This solution iterates through the bits array, using a pointer to track the current position. 
It moves the pointer based on whether it encounters a 0 (one-bit character) or a 1 (two-bit character). 
The loop continues until the pointer reaches the second-to-last bit. 
Finally, it checks if the pointer is at the last bit to determine if the last character is a one-bit character.  
"""