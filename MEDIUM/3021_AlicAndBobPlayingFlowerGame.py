"""
Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.

The game proceeds as follows:

Alice takes the first turn.
In each turn, a player must choose either one of the lane and pick one flower from that side.
At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

Alice must win the game according to the described rules.
The number of flowers x in the first lane must be in the range [1,n].
The number of flowers y in the second lane must be in the range [1,m].
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.
"""

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n * m // 2

"""
This code defines a solution to determine the number of possible pairs (x, y) of flowers in two lanes such that Alice wins the game.
The `flowerGame` method takes two integers, n and m, which represent the maximum number of flowers in the first and second lanes, respectively.
The key observation is that Alice can only guarantee a win if the total number of flowers (x + y) is odd. This is because Alice takes the first turn, and if the total number of flowers is odd, she will always be the one to pick the last flower, thus winning the game.
To find the number of valid pairs (x, y) where 1 <= x <= n and 1 <= y <= m, the method calculates the total number of pairs (n * m) and divides it by 2 to account for the pairs where the sum is even (which would result in Bob winning).
Finally, it returns the number of pairs where Alice wins.
The time complexity of this solution is O(1) since it involves only a few arithmetic operations, and the space complexity is also O(1) as it uses a constant amount of space.
"""