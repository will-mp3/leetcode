"""
You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. 
You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. 
Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.
"""

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        p, t, res = 0, 0, 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                res += 1
                t += 1
                p += 1
            else:
                t += 1

        return res

"""
this solution uses the two pointer technique to repeatedly check and pair players and trainers.
we start by first sorting our two arrays so that we can approach the problem greedily.
while both of our pointers are in bounds we check one condition.
if the current player element is less than or equal to the current trainer element, we can pair the two and move on.
we do this by incrementing result and moving each pointer one element forward.
if the current player is greater than (else) the current trainer, we need to shift the trainer pointer and search for a better trainer.
this solution runs in O(n) linear time.
"""