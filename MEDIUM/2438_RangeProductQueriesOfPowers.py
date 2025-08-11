"""
Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. 
The array is sorted in non-decreasing order, and there is only one way to form the array.

You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. 
Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. 
Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.
"""

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        strBin = reversed(str(bin(n)))

        val = 1
        powers = []
        for char in strBin:
            if char == "1":
                powers.append(int(val))
            val *= 2
        print(powers)

        res = []
        for query in queries:
            cur = 1
            for i in range(query[0], query[1] + 1):
                cur *= powers[i]
            res.append(cur%MOD)
        
        return res

"""
This code defines a solution to the problem of calculating the product of powers of 2 that sum to a given integer n for specified ranges in the queries.
The `productQueries` method first converts the integer n into its binary representation, identifying the powers of 2 that contribute to n. 
It then stores these powers in a list called `powers`. For each query, it calculates the product of the specified range of powers and appends the result to the `res` list, applying the modulo operation to handle large numbers.
Finally, it returns the list of results for all queries.
The time complexity is O(m * k), where m is the number of queries and k is the average length of the range in each query, as it computes the product for each specified range.
"""