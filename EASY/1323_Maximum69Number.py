"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        string = str(num)
        for i in range(len(string)):
            if string[i] == "6":
                string = string[:i] + "9" + string[i + 1:]
                break
        return int(string)

"""
This code defines a solution to find the maximum number that can be obtained by changing at most one digit in a given positive integer num, which consists only of the digits 6 and 9.
The `maximum69Number` method converts the integer num to a string and iterates through each character in the string. 
If it finds a '6', it replaces it with '9' and breaks out of the loop, ensuring that only the first occurrence of '6' is changed. 
Finally, it converts the modified string back to an integer and returns it.
The time complexity of this solution is O(n), where n is the number of digits in num, since it may need to check each digit until it finds a '6'.
"""