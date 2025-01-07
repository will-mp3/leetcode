"""
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. 
Answers within 10-5 of the actual answer will be accepted.
"""

class MedianFinder:

    def __init__(self):
        # two heaps, large and small
        # large is a min heap, small is a max heap
        # heaps must should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # note: we multiply our max heap by -1 to get its true value since python only declares min heaps
        heapq.heappush(self.small, -1 * num) # python only implements min heaps, we multiply by -1 to simulate a max heap

        # make sure every element in small <= every element in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]): # (-1 * self.small[0]) is the largest value in small, self.large[0] is the smallest number in large
            val = -1 * heapq.heappop(self.small) # pop largest value from small heap, store it in val
            heapq.heappush(self.large, val) # push the largest value in small to large

        # size difference handling
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small) # pop largest value from small heap, store it in val
            heapq.heappush(self.large, val) # push the largest value in small to large
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) # pop largest value from small heap, store it in val
            heapq.heappush(self.small, -1 * val) # push the largest value in small to large
        

    def findMedian(self) -> float:
        # odd length handling, returns middle value
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # even length handling, returns middle two values average
        return (-1 * self.small[0] + self.large[0]) / 2

"""

"""