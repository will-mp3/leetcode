"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
"""

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        first = "ab" if x > y else "ba"
        second = "ba" if first == "ab" else "ab"

        # First pass: remove high priority pair
        newStr1 = self.remove_substring(s, first)
        removed = (len(s) - len(newStr1)) // 2

        # Calculate score from first pass
        res += removed * max(x, y)

        # Second pass: remove low priority pair
        newStr2 = self.remove_substring(
            newStr1, second
        )
        removed = (
            len(newStr1) - len(newStr2)
        ) // 2

        # Calculate score from second pass
        res += removed * min(x, y)

        return res

    def remove_substring(self, input, target):
        stack = []

        # Iterate through each character in the input string
        for cur in input:
            # Check if current character forms the target pair with the top of the stack
            if (
                cur == target[1]
                and stack
                and stack[-1] == target[0]
            ):
                stack.pop()  # Remove the matching character from the stack
            else:
                stack.append(cur)

        # Reconstruct the remaining string after removing target pairs
        return "".join(stack)

"""
this code defines a solution to the problem of maximizing points by removing specific substrings from a given string. 
The `maximumGain` method determines the maximum points that can be obtained by strategically removing "ab" and "ba" substrings based on their associated point values. 
The `remove_substring` method is used to efficiently remove these substrings from the input string using a stack-based approach.
The solution is designed to handle the operations in two passes, first removing the substring that yields the higher points and then the one that yields the lower points, ensuring that the maximum score is achieved. 
The use of a stack allows for efficient removal of the target substrings while maintaining the order of characters in the original string.
The time complexity of this solution is O(n), where n is the length of the input string, as each character is processed once in the stack-based removal process.
"""