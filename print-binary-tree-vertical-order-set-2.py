# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/amp/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Traversal:
    def vertical(self, root):
        mapping = {}
        def helper(root, level):
            nonlocal mapping
            if not root: return
            if level not in mapping: mapping[level] = []
            mapping[level].append(root.val)
            if root.left: helper(root.left, level-1)
            if root.right: helper(root.right, level+1)

        helper(root, 0)
        for i, key in enumerate(sorted(mapping)):
            print(i, mapping.get(key))


""" 
            25
        12      44
    10       34
                40
"""
root = TreeNode(25)
root.left = TreeNode(12)
root.right = TreeNode(44)
root.left.left = TreeNode(10)
root.right.left = TreeNode(34)
root.right.left.right = TreeNode(40)

# print(Traversal().boundary(root))
# print(Traversal().findLevel(root.right, 16))
# print(Traversal().findlevelnew(root.right, 16))
Traversal().vertical(root)
