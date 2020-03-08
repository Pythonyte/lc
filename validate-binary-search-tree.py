https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, start, end):
            if not root: 
                return True
            
            val = root.val
            if start < val < end:
                return helper(root.left, start, val) and helper(root.right, val, end)
            return False
        
        import sys
        return helper(root, -sys.maxsize, sys.maxsize)
