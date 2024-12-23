"""
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. 
Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in 
lexicographically increasing order by the new language's rules. 
If there are multiple solutions, return any of them.
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # adjacency dictionary
        adj = { c:set() for w in words for c in w } 

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1] # adjacent words
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # third mentioned base case
                return "" 
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # different characters, add to adjacency list to show order
                    break

        visit = {} # False = visited, True = visited, in current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei): # if dfs returns true a loop is detected
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return "" # true returned, found a loop
        res.reverse()
        return "".join(res)

"""
to solve this problem we will make use of topological sort, which is essentialy a reverse order dfs.
the logic behind the solution to this problem is graphing the different letter ranks and then using those ranks to return their order.
the reason we must use something like topological sort is because there may be a case where our graph messes up our orders.
for example: a -> b -> c where a also points to c
we could get this by having an input like ([a][ba][bc][c]), a becomes before b, a comes before c c comes before b.
this points a to c as well as b and allows for us to possibly return acb which is invalid.
we also must avoid any looping graphs, since that is invalid due to contradiction.
to do this we will keep track of visited nodes and nodes on the current path.
if we stumble upon a visited node and it is also on our current path, that will symbolize a loop and we will return "" for invalid solution.
one last thing to look our for is a base case in which the two adjacent words, abcd and abc, share a minimum prefix but dont follow ordering rules.
in the above case, this is invalid because the shorter of the two should come first and they share the same minimum prefix, return "".
to discuss the actual code logic, i added plenty of comment since its quite complex.
its broken into three parts, finding the order of adjaceny, the dfs function, and the use of both.
the adjacency is found in the first part by going through the ordered words, looking for where the characters are different, 
and copying the order in which they appear to the adj dictionary.
the dfs function serves to check through our adjacency list and check for loops.
it does so by marking and unmarking nodes as visited and in the current path, if a node is ever crossed thats set to true already
then a loop has been found and true is returned.
in the end we call our dfs function on every character in adj, if true is ever returned it is invalid otherwise we reverse our result and return.
"""