"""
There is a school that has classes of students and each class will be having a final exam. 
You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. 
There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. 
The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.
"""

import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate gain if we add one student
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Build max heap of (-gain, passes, total)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average
        total = sum(p / t for _, p, t in heap)
        return total / len(classes)


"""
This code defines a solution to maximize the average pass ratio of classes after assigning extra students who are guaranteed to pass.
The `maxAverageRatio` method takes a list of classes, where each class is represented by a list of two integers [passi, totali], and an integer extraStudents representing the number of extra students to be assigned.
A helper function `gain` is defined to calculate the increase in pass ratio if one extra student is added to a class. The gain is calculated as the difference between the new pass ratio and the current pass ratio.
A max heap is constructed using a list comprehension that stores tuples of (-gain, passes, total) for each class. The negative gain is used because Python's `heapq` implements a min-heap by default, and we want to simulate a max-heap.
The method then iterates for the number of extra students, popping the class with the highest gain from the heap, updating its passes and total, and pushing it back into the heap with the new gain.
Finally, the method computes the final average pass ratio by summing the pass ratios of all classes in the heap and dividing by the number of classes. It returns this average.
The time complexity of this solution is O((n + k) log n), where n is the number of classes and k is the number of extra students, due to the heap operations. The space complexity is O(n) for storing the heap.
"""