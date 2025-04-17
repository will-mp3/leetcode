"""

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