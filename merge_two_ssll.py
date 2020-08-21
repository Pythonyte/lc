# Definition for singly-linked list.
# https://leetcode.com/explore/interview/card/adobe/484/linked-list/2507/
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        final_list = current = ListNode(val='dummy')
        while l1 and l2:
            if l1.val < l2.val:
                temp, l1 = l1, l1.next
            else:
                temp, l2 = l2, l2.next

            temp.next = None
            final_list.next = temp
            final_list = final_list.next
            
        if l1:
            final_list.next = l1
        if l2:
            final_list.next = l2
        return current.next
            
        
    
        
        
