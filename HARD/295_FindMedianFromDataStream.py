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
note: the logic for this code is rather complex, I have added a profuse amount of comments in place of a code explanation here.
this problem asks us to find the median of an array, the catch is numbers continually get added.
we want to find an implementation that runs better than a brute force sorting algorithm.
assuming we used in order sort, each insertion would be O(n), which is fine, but we can do better.
instead, we use min and max heaps to sort our data, this keeps our insertions in O(logn), which is the main allure of this method.
the conceptual logic is we have a min heap and a max heap which are kept equal in length.
this allows us to be able to grab the first value of the min heap and the first value of the max heap, 
and have those values always be the middle two values.
imagine we have a min heap of [3, 4] and a max heap of [1, 2], we know the median is 3 and 2 divided by 2.
if we continue to keep our heaps the same size, we can always gather these two values using min[0] and max[0].
conversely, if the length differs by 1, we simply return the first value of whichever heap is longer.
this value is guranteed to be the middle value.
"""