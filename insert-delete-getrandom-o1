https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict: return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        # print("insert",val, "==>", self.dict, self.list)
        return True
            

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict: return False
        
        index_of_removing_element = self.dict[val]
        last_element = self.list[-1]
        # put list last element into that index 
        self.list[index_of_removing_element] = self.list[-1]
        
        # change index of last element which got swapped
        self.dict[last_element] = index_of_removing_element
        
        self.list.pop()
        del self.dict[val]
        # print("remove",val, "==>", self.dict, self.list)
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import choice
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
