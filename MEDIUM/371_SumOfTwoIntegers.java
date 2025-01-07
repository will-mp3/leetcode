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
    
  */