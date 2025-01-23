"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers 
that have each been cited at least h times.
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [0] * (n + 1)
        
        # Counting papers for each citation number
        for c in citations:
            papers[min(n, c)] += 1
        
        # Finding the h-index
        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]
        
        return k

"""

"""