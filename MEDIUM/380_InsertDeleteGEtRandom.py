"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        # add value : index into dict, append value to array
        if val in self.dict:
            return False
        self.dict[val] = len(self.list) # mapping element to its index in our array, notice order
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # retrieve an idex to delete from dict, swap last element to that position, pop last element
        if val in self.dict:
            # move last element to the index of element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        # implemented with the help of random.choice module
        return choice(self.list)

"""

"""