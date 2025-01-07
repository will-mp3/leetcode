/*
    Given two integers a and b, return the sum of the two integers without using the operators + and -.
 */

 class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = a ^ b; // xor a and b, this results in our binary string with all ones except the carry values
            b = tmp; // & a and b, this results in our binary string with just the missing carry values, we shift by 1 to put them in their correct space
        }
        return a;
    }
}

 /*
    for this solution I opted to use java since I prefer its binary arithmetic over python.
    to solve this problem we make use of binary addition, we do this using the xor and and operators.
    xor gives us a binary string with all of the 1s where a 0 and 1 have been added, specifically all of the 1s that dont require a carry.
    a carry happens when 1 and 1 are added in binary, this results in a 0 in that position and a 1 carried to the next position.
    because our xor is missing these carries, we account for this by taking the and of the strings, this gives us all the 1s that we missed.
    we must also bit shift this 1 to the left to move the carrys into their correct positions.
    both of these together simulate addition, and assume that there will be carrys.
    once we do our xor operator and have no carrys, we know that our addition is complete.
    to check for this we loop until b, our and operator, is 0.
    if b is zero it means that a and b have no overlapping 1s, and therefor there are no carrys when we xor.
    once this loop terminates we return a, the xor of the current a and b binary strings.
  */