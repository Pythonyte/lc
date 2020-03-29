# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        root = head
        def helper(node):
            nonlocal root
            if node:
                if helper(node.next) is False: return False
                if node.val != root.val: return False
                root = root.next
            return True
        
        return helper(head)
        
