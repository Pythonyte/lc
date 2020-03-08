https://leetcode.com/problems/largest-bst-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
		# set count variable that gets updated to the current max nodes found
        self.count = 0
        self.helper(root)
        return self.count
        
    def helper(self, node):
        if node:
            l_res, l_low_v, l_upp_v, l_cur_count = self.helper(node.left)
            r_res, r_low_v, r_upp_v, r_cur_count = self.helper(node.right)
            if l_res and r_res and l_upp_v < node.val < r_low_v:
                self.count = max(self.count, l_cur_count + r_cur_count + 1)
                return True, min(l_low_v, node.val), max(r_upp_v, node.val), l_cur_count + r_cur_count + 1
            else:
                return False, float("inf"), float("-inf"), 0
        else:
            return True, float("inf"), float("-inf"), 0
