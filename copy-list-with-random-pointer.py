"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    ############### # Sol1 N-Space N-Time
    def get_cloned_node(self, node, visited):
        if not node: return None, visited
        
        if node not in visited: 
            visited[node] = Node(node.val, None, None)
        return visited[node], visited

    def copyRandomListWITHSPACE(self, head: 'Node') -> 'Node':
        if head is None: 
            return head
        
        old_node = head
        new_node = Node(head.val, None, None)
        visited = {}
        visited[old_node] = new_node

        while old_node:
            new_node.random, visited = self.get_cloned_node(old_node.random, visited)
            new_node.next, visited = self.get_cloned_node(old_node.next, visited)
            
            old_node = old_node.next
            new_node = new_node.next
        
        return visited[head]

    ############### # Sol2  1-Space N-Time
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: 
            return head
        
        head_copy = head

        # Put new nodes in between list 1->2->3 will be 1->N1->2->N2->3->N3
        while head:
            new_node = Node(head.val, None, None)
            new_node.next = head.next
            head.next = new_node    
            head = head.next.next
        
        # set head for first node
        head = head_copy
        # Set randoms for new nodes
        while head:
            head.next.random = head.random.next if head.random else None
            head = head.next.next
        
        
        # Split list into old and new ones
        new_head = head_copy.next
        old_node, new_node =  head_copy, head_copy.next
        while old_node and new_node:
            old_node.next = old_node.next.next
            new_node.next = new_node.next.next if new_node.next else None
            
            # for loop traversal
            old_node = old_node.next
            new_node = new_node.next
        return new_head
    
