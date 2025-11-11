"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        for s in strs:
            ones = 0
            zeroes = 0
            for ch in s:
                if ch == "0":
                    zeroes += 1
                else:
                    ones += 1
            newdp = {}

            for k, v in dp.items():
                prevzeroes, prevones = k
                newzeroes, newones = prevzeroes + zeroes, prevones + ones
                if newzeroes <= m and newones <= n:
                    if (newzeroes, newones) not in dp:
                        newdp[(newzeroes, newones)] = v + 1

                    elif dp[(newzeroes, newones)] < v + 1:
                        newdp[(newzeroes, newones)] = v + 1
            dp.update(newdp)
        return max(dp.values())

"""

"""