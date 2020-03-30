https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode: 
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def predecessor(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val
        
        def successor(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
        if root is None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
        
        return root
