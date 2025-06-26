"""You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting 
some or no characters without changing the order of the remaining characters.
"""

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if int(s[i] + res, 2) > k:
                continue
            else: 
                res = s[i] + res

        return len(res)

"""
the key to this solution is how we read in our binary stirng s.
we know that we can include leading zeros, so the max length of our subsequence is the length of s.
what that leaves us to do is figure out the minimum amount of characters we have to remove to make s less than or equal to k.
my approach to this is by going through the string backwards and creating a new string with each character seen.
we have to be careful with how the binary string is formatted so that it reads correctly, we do this be adding new charcters to the front.
each character we see is a new largest since we are starting from the back, so we want to make sure to add these to the front to retain value.
each time we check if this new binary string is greater than k, in this case we dont add anything to our string and move on.
in the event our new string is less than or equal to k, we add the new character.
in the end we return the length of our result string.
this solution runs in O(n) linear time.
"""