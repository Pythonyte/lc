https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

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
        if root is None: return root
        q = collections.deque([root, '#'])
        curr_node, prev_node = None, None 
        while q:
            curr_node = q.popleft()
            if curr_node == '#': 
                if q: q.append('#')
                prev_node = None
                continue

            if prev_node: 
                prev_node.next = curr_node
            prev_node = curr_node

            if curr_node.left: q.append(curr_node.left)
            if curr_node.right: q.append(curr_node.right)
            
        return root


