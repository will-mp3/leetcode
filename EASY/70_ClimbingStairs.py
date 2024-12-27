"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

"""
to solve this problem we use the bottom up dynamic programming approach.
we have two decisions to make each time, and when mapped into a tree we see that the pattern is identical depending on which step you are on.
for this example lets assume n = 5, we want to know how many steps it will take from position 0.
imagine a dynamic programming array from position 0 to position 5: [0, 1, 2, 3, 4, 5] (values just for show).
starting from position 5 (the top of the stairs) this is our base case, so we insert a 1: [x, x, x, x, x, 1].
in position four there is only one way to get to position 5 since two steps will go to 6, insert a 1: [x, x, x, x, 1, 1].
this is the basis for our dynamic programming approach, now we observe position 3, how many ways can 4 get to 5 and 5 get to 5? 2 total.
insert a 2 in position 3: [x, x, x, 2, 1, 1].
same approach for position 2, 2 ways to 5 from 3 and 1 way from 4: [x, x, 3, 2, 1, 1].
continue the process until you get position o (the answer): [8, 5, 3, 2, 1, 1].
we can remove the extra memory as well by using two variables to represent the positions we add together each time (4 & 5, 3 & 4, etc).
this solution runs in O(n) linear time.
"""