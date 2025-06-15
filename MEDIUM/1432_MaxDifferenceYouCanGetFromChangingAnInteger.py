"""
You are given an integer num. You will apply the following steps to num two separate times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). Note y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.
"""

class Solution:
    def maxDiff(self, num: int) -> int:
        # first, find the max value (a) by replacing first non-nine value with 9.
        num1 = str(num)
        for x in num1:
            if x != "9":
                rep1 = x
                break
            rep1 = "9"
        num1 = num1.replace(rep1, "9")

        # now find the smallest
        num2 = str(num)
        if num2[0] == "1":
            for x in num2:
                if x != "1" and x != "0":
                    num2 = num2.replace(x, "0")
                    break
        else:
            num2 = num2.replace(num2[0], "1")

        return int(num1) - int(num2)

"""

"""