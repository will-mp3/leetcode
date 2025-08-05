"""
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.
"""

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0

        for fruit in fruits:
            for basket in baskets:
                if fruit <= basket:
                    baskets.remove(basket)
                    break

        return len(baskets)

"""
This code defines a solution to determine the number of unplaced fruit types after attempting to allocate them to baskets based on their capacities.
The `numOfUnplacedFruits` method iterates through each fruit type and checks if it can be placed in any of the available baskets. 
If a fruit can fit into a basket, that basket is removed from the list of available baskets to prevent further allocations. 
If a fruit cannot be placed in any basket, it remains unplaced, and the method continues to the next fruit.
Finally, the method returns the number of remaining baskets, which represents the number of unplaced fruit types.
The time complexity of this solution is O(n * m), where n is the number of fruits and m is the number of baskets, as it checks each fruit against all baskets.
This approach ensures that all possible placements are considered, leading to an accurate count of unplaced fruits.
"""