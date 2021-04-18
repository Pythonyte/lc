# https://leetcode.com/problems/design-hashmap/submissions/
class Bucket:
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                return
        else:
            self.bucket.append((key, value))

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket.pop(i)
                return

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_space = 2079
        self.hashmap = [Bucket() for _ in range(2079)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.hash_space
        self.hashmap[index].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.hash_space
        return self.hashmap[index].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.hash_space
        self.hashmap[index].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
