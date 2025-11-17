"""
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
"""

class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    count, flag = 0, False

    for num in nums:
      if flag and num == 0:
        count += 1
      elif flag and num == 1:
        flag = not flag
        if count < k:
          return False
        count = 0
      
      if num:
        flag = not flag
    
    return True

"""
This solution iterates through the binary array while maintaining a count of zeros between consecutive 1's. 
When a 1 is encountered, it checks if the count of zeros since the last 1 is at least k. 
If not, it returns False. If the loop completes without finding any violations, it returns True. 
"""