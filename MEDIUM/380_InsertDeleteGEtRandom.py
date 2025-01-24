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
to solve this problem we will make use of two data structures, an array list and a hash map (list & dict).
our dictionary can handle insertion and deletion in constant time, but struggles with getRandom.
our list struggles with deletion but is great for get random.
we will need to ensure these structs are linked together, we start by initiating them both empty.
for insert, we check if the val is in our set already, if its not we map val:index in our dict and append val to our list.
to remove, we need to swap the item at the end of the array with our desired removal element so we can pop in constant time.
to do this we start by getting the last element and the index of the value to be removed.
we get the last element from our list and the index from our dictionary of values and indexes.
we set the element at this index in our array equal to the last element, overwriting it, and update the last element index in the dict.
we then pop the duplicate last element from the end of our list and remove the original val from the dictionary.
getRandom is much easier with the help of the random.choice module.
this entire implementation runs in O(1) constant time.
"""