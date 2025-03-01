"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities 
(this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbors
        # count outgoing edges

        edges = { (a,b) for a, b in connections }
        neighbors = { city:[] for city in range(n) }
        visit = set()
        change = 0

        # fill neighbors hashmap
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, change

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                # check if this neighbor can reach city zero
                if (neighbor, city) not in edges:
                    change += 1
                visit.add(neighbor)
                dfs(neighbor) # check if neighbor's neighbor can reach city zero

        visit.add(0)
        dfs(0)

        return change

"""
this problem is based around graph comprehension.
we know that we are given n cities and n - 1 roads which are connected as defined by our connections list.
we can view the citys as nodes and the roads as edges and use an adjacency list in the form of a hash map to track them.
we want to count the amount of cities which are not connected to their neighbors and return that value.
we can accomplish this using our graph of nodes and a depth first search algorithm to recursively check each node.
each iteration we check to see of our node and its neighbors are connected, and if not we add 1 to our count.
to start we define our edges hashmap which contains the links between nodes.
we also make a neighbors hashmap which maps the city (node) to its neighbors.
we also keep track of a visit set to avoid repeated work.
once made we create our dfs function, we go through each node in neighbors, first checking if its been visited.
if so, we continue to the next iteration.
otherwise we check if the neighbor and our current city are a present edge, if not we increment our counter variable.
every iteration we add our neighbor to the visted set and call our dfs function on the current neighbor to continue searching the graph.
we start at city 0 and return our counter variable change once the dfs completes.
this solution runs in O(n) linear time.
""" 