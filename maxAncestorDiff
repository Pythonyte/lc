https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(root):
            if root is None: return []
            left = dfs(root.left)
            right = dfs(root.right)
            combined = left + right

            for num in combined:
                nonlocal ans
                ans = max(ans, abs(root.val - num))

            combined += [root.val]
            
            if min(combined) == max(combined):
                return [min(combined)]
            else:
                return [min(combined), max(combined)]

        
        dfs(root)
        return ans
