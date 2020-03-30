https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/507/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetricRecursive(self, root: TreeNode) -> bool:
        def helper(lnode, rnode):
            if not lnode and not rnode:
                return True
            if not lnode or not rnode:
                return False
            return lnode.val == rnode.val and helper(lnode.right, rnode.left) and helper(lnode.left, rnode.right)
        return helper(root, root)

    
    def isSymmetricIterative(self, root: TreeNode) -> bool:
        q = collections.deque([root, root])
        while q:
            node_tree1 = q.popleft()
            node_tree2 = q.popleft()
            if not node_tree1 and not node_tree2:
                continue
            elif not node_tree1 or not node_tree2:
                return False
            elif node_tree1.val != node_tree2.val:
                return False
            else:
                q.append(node_tree1.left)
                q.append(node_tree2.right)
                q.append(node_tree1.right)
                q.append(node_tree2.left)
        return True
