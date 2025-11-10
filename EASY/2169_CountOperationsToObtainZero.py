"""
You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0.
"""

class Solution:
  def countOperations(self, num1: int, num2: int) -> int:
    res= 0
    while num1 and num2:
      if num1 >= num2:
        num1 -= num2
        res += 1
      else:
        num2 -= num1
        res += 1
    return res

"""
This solution implements a straightforward approach to count the number of operations required to reduce either num1 or num2 to zero. 
It uses a while loop that continues as long as both num1 and num2 are non-zero. 
In each iteration, it checks which number is larger and subtracts the smaller number from the larger one, incrementing the operation count each time. 
The process continues until one of the numbers becomes zero, at which point the function returns the total count of operations performed.
"""