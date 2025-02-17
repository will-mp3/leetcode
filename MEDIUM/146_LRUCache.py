"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # left = least recent, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # helper functions remove and insert
    # remove from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val # keys are mapped to nodes
        return -1 # default return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # create and insert new node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check capacity
        if len(self.cache) > self.cap:
            # remove LRU from list and delete from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

"""
this implementation makes use of a few different structures.
namely, we use both a linked list and hashmap to keep track of the least recent value and ensure constant time retrieval.
our hashmap will map keys to the specific nodes in our LL instead of the values for easy removal and updating.
we also create left and right sentinel nodes in our LL, these allow for constant time removal of the LRU value.
our left node will always point to our least recently used value and our right node will point to our most recently used value.
we also keep track of our capacity to ensure if its ever crossed we know to remove the LRU value.
our cache has a few methods and helper methods, with get and put being our main methods.
the helper methods remove and insert remove a given node and insert a given node at the rightmost position respectively.
the get method gets the value based on a given key, if it exists.
if key is in our cache we update it to the most recent and return the value associated with the key, otherwise return -1.
we update using our remove and insert helper variables, essentially we remove the node and add it again, making it the most recent.
our put method adds a new key value pair to our cache.
first it checks if the key is already in our cache, if it is remove the node associated with the given key.
we create a new node and add it to our cache, mapping it to its key.
we then use our insert helper function to insert the node into our LL.
after this is done we check to see if the capacity has been breached.
if so we get our LRU and remove it from the list and delete it from the cache.
"""