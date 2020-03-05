https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        output = []
        if root is None: return output
        curr_level = [root]
        while curr_level:
            next_level = []
            for node in curr_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            output.append(curr_level[-1].val)
            curr_level = next_level
        return output
            
