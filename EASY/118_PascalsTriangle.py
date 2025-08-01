"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        for i in range(1, numRows):
            cur = [0 for _ in range(i + 1)]
            cur[0], cur[-1] = 1, 1
            
            for j in range(1, i):
                cur[j] = res[i - 1][j] + res[i - 1][j - 1]
                
            res.append(cur)

        return res

"""
This code defines a solution to generate the first numRows of Pascal's triangle.
The `generate` method initializes the triangle with the first row containing a single element, 1. 
It then iterates from 1 to numRows - 1, constructing each subsequent row based on the previous row.
For each row, it initializes a new list with zeros, sets the first and last elements to 1, and fills in the middle elements by summing the two elements directly above from the previous row.
Finally, it appends the constructed row to the result list and returns the complete triangle.
The time complexity of this solution is O(n^2), where n is the number of rows, as each row requires O(i) operations to construct, leading to a total of O(1 + 2 + ... + n) operations.
This approach efficiently builds Pascal's triangle iteratively, ensuring that all rows are correctly formed based on the properties of the triangle.
"""