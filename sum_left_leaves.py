# Definition for a binary tree node.
# https://leetcode.com/explore/interview/card/adobe/490/trees-and-graphs/2538/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum_leaves = 0
        
        def helper(node, is_left):
            if not node:return    
            if is_left and not node.left and not node.right:
                nonlocal sum_leaves
                sum_leaves += node.val
            helper(node.left, True)
            helper(node.right, False)
        
        helper(root, False)
        return sum_leaves
