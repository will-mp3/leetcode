"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # check if either is zero, return False if so
        if "0" in [num1, num2]:
            return "0"

        # allocate result array and reverse our given numbers
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = (res[i1 + i2] % 10)

        # reverse result and set beginning pointer
        res, beg = res[::-1], 0
        # increment beg to remove leading zeros
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # convert to array of strings
        res = map(str, res[beg:])
        return "".join(res)

"""
this problem asks us to multiple strings without the use of built in libraries to convert the string directly.
to accomplish this we make use of old-school integer multiplication, each position multiplied by each position with carry values etc.
to start we check the edge case where a zero is given.
once thats out of the way we allocate our result array and reverse both of our number arrays for ease of arithmetic.
next we next a for loop to go through all digits in num1 and num2, this will allow that multiplication mentioned prior.
for each iteration we calculate our digit by multiplying the numbers at our current i1 and i2 indices.
once we get our digit we go through three steps:
first we add our digit value to the index i1 + i2.
next we add any carry values to the following index using integer division by 10.
lastly, we set that original i1 + i2 index equal to the current value at its position mod 10.
these steps accoutn for carry values, double digit values, past carrys, etc.
once the nested loop completes we can reverse our result list.
note that result may possess leading zeroes once reversed, we will use a beggining pointer to accomodate for this.
we increment our beg pointer until there are no more leading zeroes then turn our result into a list of strings using map.
once done we can join our result array to one string using the join operation.
"""