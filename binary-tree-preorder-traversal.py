# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        "Root Left Right"
        stack, output = [], []
        if root is None: return output
        stack = [root]
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        
        return output
