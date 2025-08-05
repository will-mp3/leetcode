"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        res = 0
        count = defaultdict(int)

        for end in range(len(fruits)):
            count[fruits[end]] += 1

            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1

            res = max(res, end - start + 1)

        return res

"""
This code defines a solution to the problem of collecting the maximum number of fruits from a row of trees while adhering to the constraints of using two baskets for different types of fruits.
The `totalFruit` method uses a sliding window approach to maintain a count of the types of fruits currently in the baskets. 
It iterates through the array of fruits, expanding the window by moving the `end` pointer and updating the count of fruits. 
If the count exceeds two types, it shrinks the window from the left by moving the `start` pointer until only two types remain.
The maximum number of fruits collected is updated at each step, and finally, the method returns this maximum value. 
The time complexity is O(n), where n is the length of the `fruits` array, as each element is processed at most twice (once when added and once when removed).
"""