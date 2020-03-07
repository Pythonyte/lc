https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/
https://leetcode.com/problems/inorder-successor-in-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def get_min_val(node):
            while node:
                succ = node
                node = node.left
            return succ
            
        if p is None: return None
        succ = None
        if p.right:
            return get_min_val(p.right)
        
        # Start from root and search for successor down the tree     
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        
        return succ
