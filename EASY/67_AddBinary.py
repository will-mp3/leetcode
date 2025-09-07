"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

"""
This code defines a solution to add two binary strings and return their sum as a binary string. The function `addBinary` takes two strings `a` and `b`, which represent binary numbers, as input and returns a string representing their sum in binary format.
The method first converts the binary strings `a` and `b` to integers using the `int` function with a base of 2. It then adds these two integers together. The result is converted back to a binary string using the `bin` function, which returns a string prefixed with '0b'. To obtain the final binary string without the '0b' prefix, the method slices the string starting from the third character using `[2:]`.
The time complexity of this solution is O(max(len(a), len(b))), as the conversion of binary strings to integers and the addition operation depend on the length of the longer string. The space complexity is also O(max(len(a), len(b))) due to the storage of the integer representations of the binary strings.
"""