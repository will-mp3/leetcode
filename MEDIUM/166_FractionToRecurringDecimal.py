"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)

        fraction.append(".")
        map_dict = {}
        while remainder != 0:
            if remainder in map_dict:
                fraction.insert(map_dict[remainder], "(")
                fraction.append(")")
                break
            map_dict[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor

        return "".join(fraction)

"""
This code defines a solution to convert a fraction represented by a numerator and denominator into its string representation, including handling repeating decimal parts. The function `fractionToDecimal` takes two integers, `numerator` and `denominator`, as input and returns a string representing the fraction. The approach used in this solution can be broken down into the following steps:
1. Handle the case where the numerator is zero, returning "0" immediately.
2. Initialize an empty list `fraction` to build the resulting string. Determine the sign of the result based on the signs of the numerator and denominator, appending a "-" if the result is negative.
3. Calculate the integer part of the fraction by performing integer division of the absolute values of the numerator and denominator. Append this integer part to the `fraction` list.
4. Calculate the initial remainder of the division. If the remainder is zero, return the current string representation as there is no fractional part.
5. Append a decimal point to the `fraction` list to indicate the start of the fractional part.
6. Use a dictionary `map_dict` to track the positions of remainders to identify repeating cycles. While the remainder is not zero, check if the remainder has been seen before:
   - If it has, insert an opening parenthesis at the position where this remainder first appeared and append a closing parenthesis at the end of the `fraction` list, then break the loop.
   - If it hasn't, store the current position of the remainder in `map_dict`, multiply the remainder by 10, and append the next digit of the fractional part to the `fraction` list. Update the remainder accordingly.
7. Finally, join the elements of the `fraction` list into a single string and return it.
The time complexity of this solution is O(n), where n is the number of digits in the fractional part, as it processes each digit at most once. The space complexity is also O(n), due to the storage of the `fraction` list and the `map_dict` dictionary for tracking remainders.
"""