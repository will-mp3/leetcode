"""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, 
you realize that there are many different ways you can decode the message 
because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. 
If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)

"""
to solve this problem we use a recursive function.
this basic approach is that given a string of ints to decode, we need to account for every combination of single and double digit values.
these values can go up to 26, since we are letter decoding.
this introduces a few edge cases, the first of which being if the string starts with zero, this cannot be since there is no 0th letter.
this is accounted for alongside the basecase if i in dp which accounts for the case in which i has already been cached
or is the last position in the string.
we then call dfs on i + 1 since we took the value at i as a single digit (this pushes us through the string).
we also have a second case where we take i as a double digit value and call dfs on i + 2.
this can happen if theres enough length left in the string AND its less than 26.
we return dfs(0) ultimately to return all the ways we can decode (every value is 1, so as the function runs it adds 1 for every valid index).
this solution runs in O(n) linear time.
"""