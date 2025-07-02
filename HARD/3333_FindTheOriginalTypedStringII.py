"""
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.
"""

class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        # edge case
        if not word:
            return 0

        # count letter groups
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # get total original strings
        total = 1
        for num in groups:
            total = (total * num) % self.MOD

        # if there are atleast k groups, return the total possible
        if k <= len(groups):
            return total

        # setup dp array
        dp = [0] * k
        dp[0] = 1
        
        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp

        invalid = sum(dp[len(groups):k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD

"""
this solution uses dynamic programming to count the number of possible original strings that Alice might have intended to type.
The approach involves counting the number of groups of consecutive characters in the input string and then calculating the total number of possible original strings based on these groups.
The function first counts the groups of consecutive characters in the input string and stores their lengths in a list called `groups`. 
It then calculates the total number of original strings by multiplying the lengths of these groups.
If the number of groups is less than k, it returns the total possible strings.
Otherwise, it uses a dynamic programming approach to calculate the number of valid strings of length at least k by iterating through the groups 
and updating a dp array that keeps track of the number of valid strings for each length.
Finally, it subtracts the invalid strings from the total and returns the result modulo 10^9 + 7.
The time complexity of this solution is O(n * k), where n is the length of the input string and k is the given positive integer. The space complexity is O(k) due to the dp array used for dynamic programming.
"""