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

"""