"""
You are given a 0-indexed string s of even length n. 
The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        close, maxClose = 0, 0

        for c in s:
            if c == "[":
                close -= 1
            else:
                close += 1
            maxClose = max(close, maxClose)
        
        return (maxClose + 1) // 2

"""
unlike a lot of the previous balanced string problems where a stack was used, this time we take a different approach.
this problem only asks us to return the minimum amount of swaps needed to balance and gurantees there is an even number of bracket types.
knowing this our approach is very simple, we will use one pass to count the amount of closed brackets.
specfically we will count and track the max amount of excess closed brackets to open brackets.
for example if we have count through four brackets and three of them are closed then we know we have an excess of 2.
we use the variable close to track and increment/decrement this and maxClose to keep track of the max amount.
we run through the characters in s, decrementing close when we find an open bracket and incrementing when we find a closed.
each iteration we update our max close value and once finished we return maxClose + 1 // 2.
this is because each swap actually removes two excess closed brackets, not one, so we account for that using integer division.
this solution runs in O(n) linear time.
"""