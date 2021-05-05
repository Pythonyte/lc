# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        # Store Undirected Graph for all connected nodes 
        conn = defaultdict(list)
        
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)   
                conn[child.val].append(parent.val)   
            if child.left:connect(child, child.left)
            if child.right:connect(child, child.right)
        
        connect(None, root)
        #print(conn)
        
        # We got the graph in conn adj list
        # we have to do level order traversal (BFS) starting from target vertex upto level K
        output, visited = [], [target.val] 
        current_level = [target.val]
        for _ in range(K):
            new_level = []
            for node in current_level:
                for val in conn[node]:
                    if val not in visited:
                        new_level.append(val)
                        visited.append(val)
                
            current_level = new_level
        print(current_level)
        
        return current_level
