"""
You are given an array of integers nums. Perform the following steps:

Find any two adjacent numbers in nums that are non-coprime.
If no such numbers are found, stop the process.
Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
Repeat this process as long as you keep finding two adjacent non-coprime numbers.
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.
"""

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = (stack.pop() * num) // g
            stack.append(num)

        return stack

"""
This code defines a solution to replace adjacent non-coprime numbers in an array with their Least Common Multiple (LCM) until no such pairs remain. The function `replaceNonCoprimes` takes a list of integers `nums` as input and returns the modified list after performing the specified operations.
The approach used in this solution can be broken down into the following steps:
1. Initialize an empty list `stack` to keep track of the numbers as they are processed.
2. Iterate through each number `num` in the input list `nums`.
3. For each number, enter a while loop that continues as long as there are elements in the `stack`.
4. Inside the loop, calculate the Greatest Common Divisor (GCD) of the last number in the `stack` (i.e., `stack[-1]`) and the current number `num` using the `gcd` function.
5. If the GCD is 1, it means the two numbers are coprime, and the loop breaks, allowing the current number to be added to the stack.
6. If the GCD is greater than 1, it means the two numbers are non-coprime. In this case, calculate the LCM of the two numbers using the formula `LCM(a, b) = (a * b) / GCD(a, b)`, update `num` to this LCM value, and remove the last number from the `stack` using `stack.pop()`.
7. After exiting the while loop, append the current number `num` (which may have been updated to an LCM) to the `stack`.
8. After processing all numbers in `nums`, return the `stack`, which now contains the final modified array.
The time complexity of this solution is O(n log m), where n is the number of elements in the input list and m is the maximum value of the elements, due to the GCD calculations. The space complexity is O(n) in the worst case, as the stack may contain all elements from the input list.
"""