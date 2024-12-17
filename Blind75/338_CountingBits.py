"""
Given an integer n, return an array ans of length n + 1 such that 
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
        
        return ans

"""
the key to solving this problem lies in dynamic programming and understanding the binary bit patterns of each value.
to solve this problem we make use of an offset variable, which is the current most signifcant bit.
we use the equation 1 + ans[i - offset] to calculate the amount of 1s based on the pattern.
the pattern of each value (starting at 1) and the equation with the offset is:
0001 (1 + (1 - 1)) = 1
0010 (1 + (2 - 2)) = 1
0011 (1 + (3 - 2)) = 2
0100 (1 + (4 - 4)) = 1
using a simple for loop and updating our offset every time it doubles (new most significant bit) we are able to return our answer.
this solution runs in O(n) linear time.
"""