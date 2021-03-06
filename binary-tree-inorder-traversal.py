# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def push_lefts_in_stack(self, root):
        # push all level leftest in stack
        while root:
            self.stack.append(root)
            root = root.left
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.output, self.stack = [], []
        if root is None: return self.output
        
        self.push_lefts_in_stack(root)

        # Pop from element and push its right and all left childs of right
        while self.stack:
            node = self.stack.pop()
            self.output.append(node.val)
            self.push_lefts_in_stack(node.right)
        
        return self.output
