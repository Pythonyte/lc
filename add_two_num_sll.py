# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/explore/interview/card/adobe/484/linked-list/2505/

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = head = ListNode(val='dummy')
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l3.next = ListNode(val=carry%10)
            l3 = l3.next
            carry //= 10
        return head.next
            
# If numbers are in normal order:
# Need more optimization and not yet completed
    def addLLOrdered(self, l1, l2):
        def helper(l1, l2):
            nonlocal carry, l3
            if None in (l1, l2):
                return
            helper(l1.next, l2.next)
            carry = l1.val + l2.val + carry
            l3.next = Node(carry%10)
            carry = carry//10
            l3 = l3.next

        l3 = head = Node(-1)
        carry = 0
        helper(l1,l2)
        if carry: l3.next = Node(carry)
        if head.next:
            new_head = self.reverselliterative(head.next)
            return new_head



#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         l3 = ListNode(val='dummy')
#         head = l3
#         carry = 0
    
#         while l1 and l2:
#             total = l1.val + l2.val + carry
#             if total >= 10:
#                 val, carry = total % 10 , total // 10
#             else:
#                 val, carry = total, 0
            
#             l3.next = ListNode(val=val)
#             l3, l2, l1 = l3.next, l2.next, l1.next
        
#         while l1:
#             total = l1.val + carry
#             if total >= 10:
#                 val, carry = total % 10 , total // 10
#             else:
#                 val, carry = total, 0
            
#             l3.next = ListNode(val=val)
#             l3, l1 = l3.next, l1.next
        
#         while l2:
#             total = l2.val + carry
#             if total >= 10:
#                 val, carry = total % 10 , total // 10
#             else:
#                 val, carry = total, 0
            
#             l3.next = ListNode(val=val)
#             l3, l2 = l3.next, l2.next
#         if carry:
#             l3.next = ListNode(val=carry)
            
#         return head.next
