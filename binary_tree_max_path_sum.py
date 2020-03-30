https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2981/
Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        
        def helper(node):
            if not node:
                return 0
            
            left_sum = max(helper(node.left), 0)
            right_sum = max(helper(node.right), 0)
            
            curr_sum = node.val + left_sum + right_sum
            nonlocal max_sum
            max_sum = max(max_sum, curr_sum)
            
            return node.val + max(left_sum, right_sum)
        
        helper(root)
        return max_sum
