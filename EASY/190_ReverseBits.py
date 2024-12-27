"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. 
In this case, both input and output will be given as a signed integer type. 
They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << 31 - i) 

        return res

"""
this problem utilizes bit shifting and both the logical AND and OR operators for its solution.
we start with our result set to zero, a 32 bit binary string of zeros for our purposes.
we create a loop that runs 32 times and complete all of our logic within it.
we first calculate whether the rightmost bit of n is a 1 or a zero using the logical AND operator.
at the same time we are shifting n to the right i bits, this allows us to check every single bit in n starting from the rightmost bit.
we then take the calculated bit and logical OR is with result, if bit is a 1 it replaces the bit in result with 1 and vice verse with 0.
to reverse these bits we this time shift our bit 31 - i bits to the left, which when i == 0 is the leftmost bit.
this logic works identically to that above, just backwards.
once the loop finishes all bits should have been correctly replaced.
this function runs in O(1) constant time because the input is always 32 bits. (if modified to handle larger ints it will be O(n)).
"""