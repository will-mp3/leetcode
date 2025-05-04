"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list) # inserted values default to list
        wordList.append(beginWord) # add begin word to wordList

        for word in wordList: # for every word in the list
            for j in range(len(word)): # for every character in the word
                pattern = word[:j] + "*" + word[j + 1:] # replace the jth character with a wildcard
                nei[pattern].append(word) # map words with this pattern in our neighbor dict

        visit = set([beginWord]) # track visited
        q = deque([beginWord]) # add first word (beginWord) to our queue for bfs
        res = 1

        while q: # while the queue isnt empty
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: 
                    return res
                # get word's neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]: # check every neighbor word in pattern dict
                        if neiWord not in visit: # check if neighbor already visted
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1 # increment by 1 after every layer

        return 0 # if we dont find the end word return 0

"""
this problem has a few things going on, the backbone is an adjacency list we create using wildcard patterns.
the idea here is we want to turn this into a graph problem since we are dealing with shortest paths.
our graph would have words who share a single letter difference connected, to simulate this we create patterns of words with one wildcard.
for example cog would have patterns [*og, c*g, co*], and dog would have patterns [*og, d*g, do*].
cog and dog would be neighbors since they possess atleast one similar pattern.
this adjacency list/graph is created using a dictionary, where patterns have the appropriate words mapped to them.
following the example above we could expect to see *og : [cog, dog].
now that we have a graph setup, we can use breadth first search to effeciantly find the shortest path to our end word.
we setup our bfs like we usually would: a visited set (with begin word added), the q (with begin word added), and our result variable.
our bfs logic is as follows:
while our queue isnt empty we go through each layer using a for loop, after each layer we add 1 to our result.
inside the layer we pop our queue and save the word to a variable.
if this word is our endWord we return result immediately, otherwise we go through all of the characters in our word to create patterns again.
for each pattern we check if there are any neighbors (if our current pattern is in our neighbor dict).
we also check if its been visited, if not we add it to visited and add the neighbor to our queue.
if result is never returned while our queue is active then return 0.
"""