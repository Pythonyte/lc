    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """
        We will do a reverse inorder traversal and keep the track of current visited node. 
        Once we found the element, last tracked element would be our answer.

        """
        last_tracked_node = None
        succ = None
        def reverse_inorder(node):
            nonlocal last_tracked_node
            nonlocal succ
            
            if node is None: 
                return None
            
            reverse_inorder(node.right)
            
            if node.val == p.val:
                succ = last_tracked_node
            
            last_tracked_node = node
            reverse_inorder(node.left)
            
        reverse_inorder(root)
        return succ
            
