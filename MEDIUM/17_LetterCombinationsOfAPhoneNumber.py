"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        
        return res

"""
this solution makes use of an imbedded recrusive function and the backtracking technique.
notice that we must hardcode a hashmap with the letter character mappings, this is ugly but unavoidable.
the recursive function is rather simple.
the base case is when our current strings length is equal to that of digits. 
this is because we are looking for encoded combos so three digits could never yield more than three characters.
while this base case is not true we iterate through all of the possible characters for each digit in digits.
we iterate through digits usng variable i which is incremented with each recursive call.
what this is essentially doing is for every character of every digit given.
for example, if our first digit (digits[0]) was 2, then we would look through all characters mapped to digits[0].
this idea continues as we move i with each succesive recursive call.
ultimately the length of digits will be hit and we append the current string which we have been updating with each c in the loop.
we call backtrack only if digits exists starting with i = 0 and curStr empty then return our res once the recursive stops.
"""