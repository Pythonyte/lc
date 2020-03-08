# https://leetcode.com/problems/boundary-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        output = []
        
        def addval(node):
            nonlocal output
            output.append(node.val)
        
        def leaves(root):
            if root:
                leaves(root.left)
                if not root.left and not root.right:
                    addval(root)
                leaves(root.right)
        
        def leftnodes(root):
            if root:
                if root.left:
                    addval(root)
                    leftnodes(root.left)      
                elif root.right:
                    addval(root)
                    leftnodes(root.right)
        
        def rightnodes(root):
            if root:
                if root.right: 
                    rightnodes(root.right)
                    addval(root)
                elif root.left: 
                    rightnodes(root.left)
                    addval(root)
                
        if root:
            addval(root)
            leftnodes(root.left)
            leaves(root.left)
            leaves(root.right)
            rightnodes(root.right)
        
        return output
