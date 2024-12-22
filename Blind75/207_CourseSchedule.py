"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to a prereq list
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the current dfs path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = [] # if we can take it, make empty for future reference
            return True 

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

"""
to solve this problem we will use a recursive depth first search algorithm.
the way the algorithm works is in order to check if we can take a class, we must check if we can take its prereqs.
this pattern remains for said prereqs and so on and so forth.
we can take a class if it has no prereqs, so we basically are checking a class to see if its root has no prereqs.
recursively we do this using a hash map of the prereq pairs and a dfs recursive function.
the function is called and checks the base cases, if we have visited this class, that means we have a loop and there is no empty set root.
if the class has an empty set as its prereqs return true, thats a valid root.
if neither base case is activated, move onto the main logic.
we add the current class to the visited set and call this recursive function on its prereqs.
if false is ever returned (there is a loop and no valid root class with no prereqs) return false.
if false is not returned, that means we have found a root class somewhere and we can then return true.
this pops the recursive function, removing the visited classes from our visited set and setting the class in our hash map to an empty set.
this solution runs in O(n) linear time (where n is equal to n + # of prereq pairs).
"""