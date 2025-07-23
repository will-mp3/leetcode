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

"""