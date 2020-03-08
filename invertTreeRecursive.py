https://leetcode.com/problems/invert-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTreeRecursive(self, root: TreeNode) -> TreeNode:
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        q = collections.deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return root
