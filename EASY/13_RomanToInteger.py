"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0 

        map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        i = 0
        while i < len(s):
            if i + 1 == len(s):
                res += map[s[i]]
                break

            if map[s[i + 1]] > map[s[i]]:
                res += map[s[i + 1]] - map[s[i]]
                i += 2
            else:
                res += map[s[i]]
                i += 1

        return res

"""
to solve this problem we use a hash map to map the value to each roman numeral.
with this map in place we can go through the string and assess each characters value.
the catch is as we go through the string we need to check the condition if the next value is larger than the current one.
is thats the case we actually want to add the larger value minus the smaller value.
in this case we skip to characters instead of the usual one.
when we reach the end of our string, i equals len(s), we know we are done and can add the last value and return.
this solution runs in O(n) linear time.
"""