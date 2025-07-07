"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.
"""

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events based on start day
        events.sort()
        
        min_heap = []
        day = 0
        index = 0
        n = len(events)
        result = 0

        while min_heap or index < n:
            if not min_heap:
                day = events[index][0]
            # add all end times for each day
            while index < n and events[index][0] <= day:
                # add end time to heap
                heapq.heappush(min_heap, events[index][1])
                index += 1
            # increment result by 1 for each pop
            heapq.heappop(min_heap)
            result += 1
            day += 1 # move day forward
            
            # clear out expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
        
        return result

"""

"""