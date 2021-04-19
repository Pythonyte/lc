# https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/
"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        def helper(node, max_till_now):
            if not node: return
            if node.val >= max_till_now:
                max_till_now = node.val
                nonlocal good_nodes
                good_nodes += 1
            helper(node.left, max_till_now)
            helper(node.right, max_till_now)
        
        helper(root, -sys.maxsize)
        return good_nodes
