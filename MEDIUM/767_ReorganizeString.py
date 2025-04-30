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
this solution uses a heap and character counts to find its solution.
the basic algorithm is that at any point the next character we want to add to our string is the one with the most remaining instances.
this is always true except for when that same character was our previous character.
we get our character counts using the counter library, create a list maxHeap using the negative counts (python has no max heap, minheap trick).
we then use heapq.heapify to put all of our values in order.
we know that the "largest" will show as the minimum because we made everything negative.
while our heap is live and/or previous exists we loop.
each time we check our fail case, if we have a previous value but nothing remaining in the heap.
this depicts the scenario where our maxheap is empty but there is still a character to be added, 
if we had an alternating value this would have been cleared and previous set back to Null.
if this is the case return the empty string.
if not, we get our count and char variable, add the character to string, and increment count by 1 (remember these are negative counts).
we check if prev exists, if so we can push it to the heap again and reset prev to Null.
if the count is not zero we set our new prev and continue.
this solution runs in O(nlogn) thanks to the use of the heap.
"""