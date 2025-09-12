"""
Alice and Bob are playing a game on a string.

You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:

On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels.
On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels.
The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.

Return true if Alice wins the game, and false otherwise.

The English vowels are: a, e, i, o, and u.
"""

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c in 'aeiou':
                return True
        return False

"""
This problem is stupid btw.
This code defines a solution to determine the winner of a game played by Alice and Bob on a given string `s`. The game involves removing substrings based on the number of vowels they contain, with Alice starting first. The function `doesAliceWin` takes a string `s` as input and returns `True` if Alice wins the game and `False` otherwise.
The approach used in this solution is straightforward:
1. The function iterates through each character `c` in the string `s`.
2. It checks if the character `c` is a vowel by seeing if it is in the list of vowels `['a', 'e', 'i', 'o', 'u'].
3. If a vowel is found during the iteration, the function immediately returns `True`, indicating that Alice can make a move and thus will win the game.
4. If the loop completes without finding any vowels, the function returns `False`, indicating that Alice cannot make a move and will lose the game.
The time complexity of this solution is O(n), where n is the length of the string `s`, as it requires a single pass through the string to check for vowels. The space complexity is O(1) since no additional space is used that scales with the input size. 
"""