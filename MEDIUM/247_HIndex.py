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
for this problem, we make use of an array that counts the amount of papers each citation count has.
the way this is carried out is by creating an empty array of size n + 1 (to account for zero indexing) 
and incrementing each index as a citation count.
for example, if we have a paper with three citations, index three is incremented by 1.
we set up our variable n and empty array papers then iterate through the citations.
we add 1 to the index of papers found by taking the minimum of n (total amount of papers) and c (amount of citations).
the reason we use this min function is to save effeciency, because of the definition of h value, 
we know that any amount of citations above the amount of papers is redundant, so we cap citations at total paper count.
once our array is filled, we start at the end of the array, the largest amount of citations, and iterate backwards.
we continue iterating backwards through the list until s is greater than k.
for example, if we have 3 papers with 5 citations, we decrement k to 4 and add 3 to the citations at 4.
if 4 had 2 citations our s value is now 5 and this loop dosent execute and we return k, which is 4.
this solution runs in O(n) linear time.
"""