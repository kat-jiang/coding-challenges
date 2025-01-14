from collections import defaultdict
from random import choice

class RandomizedCollection:

    def __init__(self):
        """Initialize collection to hold all values, and dict to store indexes."""
        
        self.collection = []
        self.index = defaultdict(set)

    def insert(self, val: int) -> bool:
        """Inserts value into collection. Returns true if item not in collection previously."""
        
        self.index[val].add(len(self.collection))
        self.collection.append(val)
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        """Removes value from collection. Returns True if collection contained item."""
        if not self.index[val]:
            return False
        remove_idx = self.index[val].pop()
        last_value = self.collection[-1]
        
        self.collection[remove_idx] = last_value
        self.index[last_value].add(remove_idx)
        self.index[last_value].remove(len(self.collection) - 1)
        
        self.collection.pop()
        return True

    def getRandom(self) -> int:
        """Get random element from collection"""
        return choice(self.collection)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()