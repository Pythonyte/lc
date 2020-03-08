# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderSuccessorPredeccsor(self, root, p):
        """
        To find successor and predecssor both
        """
        """
        We will do a reverse inorder traversal and keep the track of current visited node. 
        Once we found the element, last tracked element would be our answer.

        """
        last_tracked_node = None
        succ, pred, is_pred = None, None, False

        def reverse_inorder(node):
            nonlocal last_tracked_node, is_pred, pred, succ

            if node is None:
                return None

            reverse_inorder(node.right)

            if is_pred:
                pred = node
                is_pred = not is_pred

            if node.val == p.val:
                succ = last_tracked_node
                is_pred = True
            last_tracked_node = node
            reverse_inorder(node.left)

        reverse_inorder(root)
        print("Pred={} | Node={} | Succ={} ".format(pred and pred.val, p and p.val, succ and succ.val))


root1 = TreeNode(50)  
root1.left = TreeNode(20)  
root1.right = TreeNode(60)  
root1.left.left = TreeNode(10)  
root1.left.right = TreeNode(30)  
root1.right.left = TreeNode(55)  
root1.right.right = TreeNode(70)
s = Solution()

s.inorderSuccessorPredeccsor(root1, root1.right.left)
s.inorderSuccessorPredeccsor(root1, root1.right.right)
s.inorderSuccessorPredeccsor(root1, root1.left.left)
s.inorderSuccessorPredeccsor(root1, root1)


# OutPut
# Pred=50 | Node=55 | Succ=60
# Pred=60 | Node=70 | Succ=None
# Pred=None | Node=10 | Succ=20
# Pred=30 | Node=50 | Succ=55
