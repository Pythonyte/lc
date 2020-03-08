https://leetcode.com/problems/lru-cache/

class LRUCache:
    class DLinkNode:
        def __init__(self, key=None, val=None):
            self.prev = None
            self.next = None
            self.val = val
            self.key = key
            
    def __init__(self, capacity: int):
        self.mapping = {}
        self.capacity = capacity
        self.current_size = 0
        self.head, self.tail = self.DLinkNode(), self.DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping.get(key)
        self.__move_node_in_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping.get(key)
            self.__move_node_in_front(node)
            node.val = value
        else:
            if self.current_size == self.capacity:
                self.__remove_node_from_end()
                node = self.DLinkNode(key=key, val=value)
                self.__add_node_in_front(node)
            else:
                node = self.DLinkNode(key=key, val=value)
                self.__add_node_in_front(node)
        
    def __move_node_in_front(self, node):
        #remove node link
        node.prev.next = node.next
        node.next.prev = node.prev

        # add at front
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def __remove_node_from_end(self):
        node_to_remove = self.tail.prev
        node_to_remove.prev.next = self.tail
        self.tail.prev = node_to_remove.prev
        del self.mapping[node_to_remove.key]
        self.current_size -= 1  

    def __add_node_in_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.mapping[node.key] = node
        self.current_size += 1
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
