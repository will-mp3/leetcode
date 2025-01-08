"""
Given a binary array data, 
return the minimum number of swaps required to group all 1's present in the array together in any place in the array.
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        l, r = 0, 0
        maxOnes = countOnes = 0

        while (r < len(data)):
            countOnes += data[r] # add possible 1
            r += 1

            if (r - l) > ones: # check if window has grown too large
                countOnes -= data[l] # subtract possible 1
                l += 1

            maxOnes = max(maxOnes, countOnes) 

        return ones - maxOnes

"""
this solution asks us to find the minimum amount of swaps to have all 1s in an array be adjacent.
to break this problem down a little we understand that we can find the amount of 1s in our array by using the sum function.
using this sum function and the sliding window technique, we can traverse our list using a window the size of the number of 1s in our array.
the reason this works is because we are essentially looking to join all of our ones together, 
so if we can find the window with the most 1s in it, then we have also found the window with the minimum amount of swaps needed.
we start by figuring out how many 1s we have, this sum function is nice but its costly so we cant use it more than once.
we initiate our left and right pointers to 0, as well as our maxOnes and countOnes variables.
we iterate through our list so long as our right pointer is in bounds, each time adding any potential 1s to our count and incrementing r.
we also check to see if our window has grown too large, remember we want it to be the size of ones.
if so, we decrement a potential 1 at our left pointer position and shift the left pointer to the right.
we then update our max count and continue this until the loop breaks.
once finished, our result is the amount of 0s in our window with the most 1s, we can return our ones count - the max ones variable.
this solution runs in O(n) linear time.
"""