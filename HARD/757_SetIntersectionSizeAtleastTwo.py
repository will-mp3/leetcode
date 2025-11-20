"""
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.
"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        nums = []
        res = 0

        for interval in intervals:
          start, end = interval[0], interval[1]
          count = 0

          for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= start and nums[i] <= end:
              count += 1
              if count == 2:
                break
          
          if count == 0:
            nums.append(end - 1)
            nums.append(end)
            res += 2
          elif count == 1:
            nums.append(end)
            res += 1
        
        return res

"""
This solution first sorts the intervals based on their end values (and start values in descending order for tie-breaking). 
It then iterates through each interval, checking how many numbers from the current containing set (nums) fall within the interval. 
If none are found, it adds the two largest possible numbers from the interval to nums. 
If one number is found, it adds the largest possible number from the interval. 
The result (res) keeps track of the total numbers added to the containing set, which is returned at the end.
"""