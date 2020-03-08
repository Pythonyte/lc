https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: 
            return None
        if root.val in [p.val, q.val]: 
            return root
        
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        # If both side is True means both side have one, one value.. so root is lca
        if left_lca and right_lca: 
            return root
        
        return left_lca if left_lca else right_lca
