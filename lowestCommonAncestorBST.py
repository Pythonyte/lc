https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return None
        max_val, min_val = max(p.val, q.val), min(p.val, q.val)
        root_val = root.val
        print(min_val, root_val,max_val)
        if min_val <= root_val <= max_val: return root
        
        if root_val < min_val: 
            return self.lowestCommonAncestor(root.right, p, q)
        elif root_val > max_val:
            return self.lowestCommonAncestor(root.left, p, q)
    
