def max_path_sum(node):
    max_sum = float('-inf')
    def helper(node):
        if not node:
            return 0
        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)
        curr_sum = node.val + left_sum + right_sum

        nonlocal max_sum
        max_sum = max(max_sum, curr_sum)

        return node.val + max(left_sum, right_sum)

    helper(node)
    return max_sum

def validbst(root):
    def helper(root, start, end):
        if not root:
            return True
        val = root.val
        if start < val < end:
            return helper(root.left, start, val) and helper(root.right, val, end)
        return False
    import sys
    return helper(root, -sys.maxsize, sys.maxsize)
