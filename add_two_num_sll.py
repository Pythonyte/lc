# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/explore/interview/card/adobe/484/linked-list/2505/
# https://leetcode.com/problems/add-two-numbers-ii/submissions/
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
            
# If numbers are in normal order(Hard Problem):
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reversell(head):
            if not head: return
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        l1 = reversell(l1)
        l2 = reversell(l2)
        l3 = l3head = ListNode('dummy')
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
            carry = carry // 10
        
        return reversell(l3head.next)
