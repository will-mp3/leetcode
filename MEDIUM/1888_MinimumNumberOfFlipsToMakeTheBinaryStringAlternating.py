"""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
"""

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s) # size of our sliding window

        # create our extended string and two extended alternating target strings
        s = s + s
        alt1, alt2 = "", ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"

        res = len(s) # initial result value

        # counters to track differences (flips needed) for alt1 & alt2
        diff1, diff2 = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            # check if window is greater than n
            if (r - l + 1) > n:
                # if there was a difference at the soon to be shifted left pointer, decrement diff count
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1

            # once the window is big enough, update our result
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
            
        return res

"""
for this solution we make use of a sliding window technique with a couple clever additions.
for starters its important to understand that there are two target strings: 
an alternating string that starts with 0 (ex: 010101) and one that starts with 1 (ex: 101010).
knowing this we can create these strings and use them to count the number of differences from our string s.
the number of differences is also the number of flips, and it is also the number of type 2 operations.
what makes this question interesting is the ability to use type 1 operations, which moves the first value to the end of the string.
we know that type 1 operations are cyclical, meaning we can do n type 1 operations before our string starts repeating.
knowing this, we can create a modified string with every possible form of s, and traverse it using a sliding window.
for example if s = 111000 we know that if we max out our type 1 operations s can look like 111000111000 with a sliding window of length s.
we set up our problem using this idea, and using our sliding window check the number of differences based on every form s can take.
note we must also duplicate our two target strings.
we start the problem by getting the length of our original string s to size our window.
we then create our new string s and our alt1 and alt2 strings which will represent our targets.
we create a result variable and create two variables to count the number of differences for alt1 and alt2.
now we can start sliding our window, each iteration we check if the values at index r are different and increment the appropriate diff count.
once our window is of size n, we check if the soon to be changed left pointer had a difference.
if so, we decrement the count and increment our left pointer.
finally, once our window is big enough we can update our result and return it.
this solution runs in O(n) linear time.
"""