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
                candy = candies[box]
                candies[box] = 0
                myBoxes.remove(box)

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

        for box in initialBoxes:
            res += dfs(box)
        
        return res

"""
both of these solutions make use of a depth first search algorithm.
the first example is the worst case time complexity that dosent make use of caching.
this solution repeatedly recruses over the boxes in the myBoxes array, which are removed once opened.
this extra recursion adds a lot of time.
the optimal solution using caching, where instead of removing boxes it adds them to a seen set.
this cuts the recursion down a lot and simplifies the solution all together.
we have a seen set for boxes we've opened and a canSee set for boxes we've seen but havent opened.
each time we check if our box has been opened, if so return 0.
then we check if the box is locked, if so add it to our canSee set and return 0.
if neither execute then we can opne our box.
add the box to seen and gather its candies.
now we go through any new boxes also in the box, call dfs on all of those boxes and add the result to candy.
now we check the keys we may have found.
for each key unlock the box in the status array.
if the key goes to a box in our canSee set, call dfs on that box and add the result to candy.
once our recursive stacks return we can return our candy value.
call dfs on every box in our initial box and return the sum of all trees.
"""