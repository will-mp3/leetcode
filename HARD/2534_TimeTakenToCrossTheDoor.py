"""
There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second.

You are given a non-decreasing integer array arrival of size n, where arrival[i] is the arrival time of the ith person at the door. 
You are also given an array state of size n, 
where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door.

If two or more persons want to use the door at the same time, they follow the following rules:

If the door was not used in the previous second, then the person who wants to exit goes first.
If the door was used in the previous second for entering, the person who wants to enter goes first.
If the door was used in the previous second for exiting, the person who wants to exit goes first.
If multiple persons want to go in the same direction, the person with the smallest index goes first.
Return an array answer of size n where answer[i] is the second at which the ith person crosses the door.

Note that:

Only one person can cross the door at each second.
A person may arrive at the door and wait without entering or exiting to follow the mentioned rules.
"""

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enterQ, exitQ = deque(), deque()
        time = 0
        prev_state = 1
        i = 0

        res = [0 for n in range(len(arrival))]
        # loop while there are still people arriving, or either queue exists
        while i < len(arrival) or enterQ or exitQ:

            while i < len(arrival) and arrival[i] <= time:

                if state[i] == 0:
                    enterQ.append(i)
                else:
                    exitQ.append(i)
                i += 1

            if prev_state == 1:
                if exitQ:
                    res[exitQ.popleft()] = time
                elif enterQ:
                    res[enterQ.popleft()] = time
                    prev_state = 0

            else:
                if enterQ:
                    res[enterQ.popleft()] = time
                elif exitQ:
                    res[exitQ.popleft()] = time
                    prev_state = 1
                else:
                    prev_state = 1

            time += 1
        
        return res

"""

"""