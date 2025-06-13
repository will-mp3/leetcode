"""
You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. 
You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically.
"""

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = {} # Union-Find dictionary to store parent of each word
        
        def union(x, y): 
            uf[find(y)] = find(x) # Merge the roots of x and y
            
        def find(x):
            uf.setdefault(x, x)  # If x is not in uf, set uf[x] = x (it is its own root)
            if uf[x] != x:
                uf[x] = find(uf[x])  # Path compression: point x directly to its root
            return uf[x]

        
        for a,b in synonyms:
            union(a, b) # Build Union-Find structure from synonym pairs
            
        d = collections.defaultdict(set)
        for a, b in synonyms:
            root = find(a)
            d[root] |= set([a, b]) # Add both a and b to the synonym set of their group root
        txt = text.split() # Split the input sentence into words
        res = []
        for t in txt:
            if t not in uf: 
                res.append([t]) # If word has no synonyms, only one choice: itself
            else:
                r = find(t)
                res.append(list(d[r])) # Replace with all synonyms from the group
        fin_res = [" ".join(sentence) for sentence in itertools.product(*res)]
        return sorted(fin_res) # Return results in lexicographical order

"""

"""