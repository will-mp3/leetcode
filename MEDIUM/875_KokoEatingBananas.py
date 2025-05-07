"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # max out solutiong can be

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # round up function

            if hours <= h: # working rate found, look for smaller rate
                res = min(res, k)
                r = k - 1
            else: # no working rate found, look for larger rate
                l = k + 1

        return res

"""
this solution relys on binary search for optimization but really builds off the brute force solution.
we know two things off the start: the minimum eating rate is 1, and the maximum eating rate is the maximum pile in piles.
the brute force solution checks every rate, 1 to max(piles), and returns the minimum of all the working rates.
if this was a left to right pass it would return the first working rate.
our solution makes use of binary search and instead starts at the middle rate k.
we calculate if k is a working rate, if it is we check our left partition for any working rates that may be smaller.
if k is not a working rate we check the right partition to find one that will work.
this pattern repeats, updating our result based on the minimum rate k found.
once complete we return result.
"""