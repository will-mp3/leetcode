"""You are given an integer n which represents an array nums containing the numbers from 1 to n in order. 
Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. 
Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.
"""

from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        # Group all `u` values by their `v` endpoint
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        # Base score
        ans = 0 
        # `left` stores [top1, top2] `u` values seen so far, where top1 >= top2.
        # `left[0]` acts as our running `forbidden_start`.
        left = [0, 0] 
        # `bonus[u]` accumulates the total gain if the critical conflict involving `u` is removed.
        bonus = [0] * (n + 1)
        
        # Single pass from r = 1 to n
        for r in range(1, n + 1):
            # Check for new conflicts ending at `r` and update `left`
            for l in right[r]:
                # This is a concise trick to update the top two seen values
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
            # Add the count for this endpoint to the base score
            ans += r - left[0]

            # The gain at this step is the difference between the top two forbidden starts.
            # We add this gain to the tally for the `u` value causing the restriction (`left[0]`).
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        # The final result is the base score plus the maximum possible gain.
        return ans + max(bonus)

"""
This code defines a solution to the problem of maximizing the number of valid subarrays after removing one conflicting pair from a list of pairs.
The `maxSubarrays` method processes the conflicting pairs and calculates the maximum number of valid subarrays by maintaining a running count of forbidden starts and potential gains from removing conflicts.
The solution efficiently groups conflicting pairs and uses a single pass to compute the base score and potential gains, ensuring that the maximum number of valid subarrays is returned.
The time complexity is O(n + m), where n is the length of the array and m is the number of conflicting pairs, making it efficient for larger inputs.
The use of a list to track the top two forbidden starts allows for quick updates and calculations, ensuring that the solution remains optimal.
This approach effectively balances the constraints imposed by conflicting pairs while maximizing the number of valid subarrays.
"""