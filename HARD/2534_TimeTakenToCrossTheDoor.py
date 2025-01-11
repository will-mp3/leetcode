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

            # fill queues with arriving people at this current second
            while i < len(arrival) and arrival[i] <= time:

                if state[i] == 0: # if state is zero, queue them to enter
                    enterQ.append(i)
                else: # if state is 1, queue them to exit
                    exitQ.append(i)
                i += 1

            if prev_state == 1: # if previous person exited
                if exitQ: # let all queued to exit
                    res[exitQ.popleft()] = time
                elif enterQ: # let all queued to enter
                    res[enterQ.popleft()] = time
                    prev_state = 0

            else: # if previous person entered
                if enterQ: # let all queued to enter
                    res[enterQ.popleft()] = time
                elif exitQ: # let all queued to exit
                    res[exitQ.popleft()] = time
                    prev_state = 1
                else: # no one in queue, set state to 1 to account for default exit priority
                    prev_state = 1

            time += 1 
        
        return res

"""
Use two deques to store all people entering and exiting before current time. 
Use a prev_state to record the previous state and update prev_state, time and res once a person passes the door.
our enter and exit rules dictate that if the door was not used in the previous second, exit gets priority.
if enter was used in the previous second, enter gets priority (same applies to exit by default).
our solution uses two loops, the overarching while loop runs so long as there are still people arriving or either queue exists.
the nested while loop fills each deque at the current time.
once the dequeues are filled we check for state. 
note that state is 1 by default since exiters are given priority if no one has used the door in the last second.
if state is 1, we let those exiting in first, then entering, and update state to 0 (last use was entering).
if state is 0, we let those entering first, then exiting, and update state to 1 (last use was exiting).
note that unlike the first if block, we have an else to update state to 1 if the queue is empty,
this symbolizes a gap in people allowing us to reset to our exit priority default.
"""