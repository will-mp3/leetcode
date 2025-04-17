"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and leave the other as original.
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # create list of chars for easy access
        chars = list(s)
        # length of string
        n = len(chars)
        
        for i in range(0, n, 2 * k): # from 0 to len(s) hopping 2k elements
            start = i
            end = min(i + k, n) # dont go past end of string
            
            chars[start:end] = chars[start:end][::-1]
            
        return "".join(chars)
    
"""

"""