https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        
        while root and root.left:
            next = root.left
            
            while root:
                root.left.next =  root.right
                root.right.next = root.next and root.next.left
                root = root.next
            
            root = next
        return head
        
