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
this solution uses a clever algorithm to find its solution.
what we are doing is running a simulation on every letter in our string.
we first and foremost gather the counts for each letter in a dictionary and set our default result to the length of the string.
for each character in our string we run a simulation as if it was the smallest count present.
doing this we know a few things:
one, if any character has less occurences, they must all be deleted.
two, if a character has more than k extra occurances, we must delete the excess occurances so that there is no greater than k.
each time we do one of these operations we add the deletions to our deleted value.
we compare this deleted value with our current result and update based on the minimum.
this is done for every character, effectively simulating every possible solution and its required deletions.
"""