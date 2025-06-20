"""
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
"""

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        
        for i in range(len(s)):
            c = s[i]
            if c == 'N':
                north += 1
            elif c == 'S':
                south += 1
            elif c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            
            x = abs(north - south)
            y = abs(east - west)
            md = x + y
            dis = md + min(2 * k, i + 1 - md) # manhanttan distance plus available changes
            ans = max(ans, dis)
        
        return ans

"""
for this solution we know that we can get an extra 2 distance for each change k we make.
we loop through our characters in s, calculating the distance each time by our incrementing directional values.
our manhattan distance is the sum of x and y.
to get the max distance we add our md with the available changes we have (min(2 * k, i + 1 - md)).
each time we update our answer with the max of itself and the new max distance.
"""