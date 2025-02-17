"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has three possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output but added to cycle
        # unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            # check for cycle
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output

"""
this solution makes use of the topological sort algorithm.
this algorithm makes use of depth first search as well as an adajaceny list to find the correct order in which courses must be taken.
the first thing we need to do is making our prereq adjacency list which contains course:[prereqs] pairs.
once this is created we initialize our output list and visit & cycle sets.
as previously mentioned we make use of depth first search in this solution so we will need to create the function for that as well.
the way this function works is by first checking two condintions.
the first is if our course is in our cycle set, if this is true we have found a cycle and must return false.
the second condition is is our course is in visit, if this is true we can return true and continue, no need to deal with it twice.
if we get through these tow conditions we add our course to our current cycle set.
next, we got hrough all of the prereqs for our current course, 
we call our dfs function on them and if False is returned ever we return False, a cycle was found.
if false is never returned we can begin cleaning up our current process.
we remove the current course from our cycle set, add it to our visit set, and append it to our output set.
finally we can return true at the end of our dfs function.
now that our depth first search function is created we need to call it.
for every course in our courseList (we use the range of numCourses since theyre represented as integers) we call our dfs function.
again if this ever returns false we know a cycle was found and must return an empty list.
if false is never returned our loop will finish and we can return out output list.
this solution runs in O(e + v) where e is the number of edges and v is the number of vertexes.
"""