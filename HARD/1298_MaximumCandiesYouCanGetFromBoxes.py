"""
You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

status[i] is 1 if the ith box is open and 0 if the ith box is closed,
candies[i] is the number of candies in the ith box,
keys[i] is a list of the labels of the boxes you can open after opening the ith box.
containedBoxes[i] is a list of the boxes you found inside the ith box.
You are given an integer array initialBoxes that contains the labels of the boxes you initially have. 
You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.
"""
class firstSolution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        myBoxes = []
        res = 0

        for i in range(len(initialBoxes)):
            myBoxes.append(initialBoxes[i])

        def dfs(box): # box received as an index
            candy = 0

            if status[box]:
                print(myBoxes)
                candy = candies[box]
                candies[box] = 0
                myBoxes.remove(box)
                print(myBoxes)

                if keys[box]:
                    for i in range(len(keys[box])):
                        status[keys[box][i]] = 1

                if containedBoxes[box]:
                    for box in containedBoxes[box]:
                        myBoxes.append(box)
                
                for box in myBoxes:
                    candy += dfs(box)
            
            return candy
        
        for box in myBoxes:
            res += dfs(box)
        
        return res


class optimalSolution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        seen = set()
        canSee = set()
        res = 0

        def dfs(box): # box received as an index

            if box in seen:
                return 0
            
            if not status[box]:
                canSee.add(box)
                return 0

            seen.add(box)
            candy = candies[box]

            for newBox in containedBoxes[box]:
                candy += dfs(newBox)

            for key in keys[box]:
                status[key] = 1
                if key in canSee:
                    candy += dfs(key)
            
            return candy

        return sum([dfs(box) for box in initialBoxes])

        for box in initialBoxes:
            res += dfs(box)
        
        return res

"""

"""