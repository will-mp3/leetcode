"""
You are given a string word and an integer k.

We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.

Return the minimum number of characters you need to delete to make word k-special.
"""

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # get our character counts
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        
        # default result, if we delete every character
        res = len(word)

        # outer loop to test each character
        for a in cnt.values():
            deleted = 0 # track deletions
            # inner loop to compare each character to our current test character
            for b in cnt.values():
                # if count of a is more than count of b, delete all of b
                if a > b:
                    deleted += b
                # if count of b is greater than a + k, delete the difference between b and a + k
                elif b > a + k:
                    deleted += b - (a + k)
            # update res
            res = min(res, deleted)

        return res

"""

"""