# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Iterative
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head
    
    # Recursive
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(curr, prev):
            if curr is None:
                self.head=prev
                return
            nxt = curr.next
            curr.next = prev
            helper(nxt, curr)
        
        helper(head, None)
        return self.head
