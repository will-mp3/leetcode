"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # hashmap, counts each character and returns hashmap with counts
        # create max heap using minheap and negatives (python has no maxheap)
        maxHeap = [[-cnt, char] for char, cnt, in count.items()] # heapify based on first key, -cnt
        heapq.heapify(maxHeap) # turn our list into a heap

        prev = None # previous used character
        res = ""
        while maxHeap or prev:
            # if previous non null and maxheap is empty, no solution
            if prev and not maxHeap:
                return ""

            # most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res

"""

"""