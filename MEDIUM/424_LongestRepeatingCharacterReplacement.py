"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # increment count for character at position r by 1, default 0 if it is not in the hash map yet

            # check if window is not valid: length of window - most frequent character 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # max between current result and current window

        return res

"""
this solution is another example of a sliding window problem.
to solve this problem we first initiate a hash map to keep track of the count for all 26 english characters as well as our left/right pointers.
the way the logic works is we go through the array of characters, counting how many of each there are and saving them in our hash map.
while our window is equal to (or greater than) the count of the most common character plus the k value, we know its valid.
for example: if our window is currently five characters long, we can make 2 replacements (k = 2), and we have 3 'B' characters, its valid.
now if it grew to six characters and went from [A,B,B,A,B] to [A,B,B,A,B,A] it would be invalid (3 + 2 = 5 !>= 6).
we continue checking this equation, and if it ever fails we move our left pointer until it is once again true, 
decrementing the count of characters we remove.
we then calculate the result based on the max of the current result and the current window size.
this solution runs in O(n) linear time.
"""