"""
You are given two string arrays username and website and an integer array timestamp. 
All the given arrays are of the same length and 
the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], 
the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], 
the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], 
the score is the number of users x such that x visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. 
If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

Note that the websites in a pattern do not need to be visited contiguously, 
they only need to be visited in the order they appeared in the pattern.
"""

from collections import defaultdict # dictionary
from itertools import combinations # gather all possible combinations, respecting order

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)

        # gather tuples, sorted by timestamp, of all our information
        for (t, u, w) in sorted(zip(timestamp, username, website)):
            graph[u].append(w) # append website to user, already in order sorted by timestamp

        scores = defaultdict(int)
        for user, websites in graph.items():
            # for every website visit order saved
            for pattern in set(combinations(websites, 3)): # all unique combinations of three websites
                scores[pattern] += 1

        # find our max pattern and count
        max_pattern, max_count = '', 0
        for pattern, cnt in scores.items():
            if cnt > max_count or (cnt == max_count and pattern < max_pattern):
                max_pattern = pattern
                max_count = cnt
        
        return max_pattern

"""
for this solution we are essentially trying to find the most repeated pattern when analyzing users web traffic.
to accomplish this we will eventually create counts based on every possible pattern across all users traffic data.
before that however, we need to get each users specific web traffic, which will require some input manipulation.
we will store this info in a dictionary, graph, and to get this information we will need ot zip our three input arrays.
we go through the now zipped and sorted, by timestamp, information and append each website visit to the user as we go.
what this does is gives each users web traffic in its time stamp order (see sorting function in our for loop).
next we create another dictionary for our patterns and their appearances, scores.
for every user and website in our original graph, and for every possible pattern in each users website traffic, increment the pattern by 1.
notice the set used to avoid duplicate patterns.
this gives us every possible pattern from every users web traffic data and the amount of times we see it (max 1 per user).
now we find our max pattern and return it.
notice we track count to see if we have a duplicate max with a smaller lexographic pattern, 
since we want to return the smallest lexographic solution.
"""