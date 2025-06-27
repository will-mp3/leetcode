"""
You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or 
no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, 
where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, 
is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, 
return the lexicographically largest one. If there is no such subsequence, return an empty string.
"""

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub: str, t: str, k: int) -> bool:
            count = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        i = 0
                        count += 1
                        if count == k:
                            return True
            return False

        res = ""
        q = deque([""])
        while q:
            curr = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                nxt = curr + ch
                if isK(nxt, s, k):
                    res = nxt
                    q.append(nxt)
        return res

"""
this solution uses breadth first search for its solution and a helper function, isK, to check if the subsequence is valid.
our function starts with a queue holding an empty string, we go through each letter a - z and see if there is k or more instances in s.
if there are, we add it to our queue, each time we add to the queue we save that as our result.
ultimately the last value added to the queue is our result (lexicographically largest and longest).
after our initial run thorugh the queue, we then start to build subsequences using a - z, each time checking them with isK like before.
this continues updating our queue until it is empty then returns our last added subsequence.
"""