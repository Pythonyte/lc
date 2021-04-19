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
            
        
    
        
def mergeTwoArrays(l1, l2):
    if not l1: return l2
    if not l2: return l1
    l3 = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            temp, i = l1[i], i+1
        else:
            temp, j = l2[j], j+1
        l3.append(temp)

    if i < len(l1):
        l3.extend(l1[i:])

    if j < len(l2):
        l3.extend(l2[j:])
    return l3

print(mergeTwoArrays([], [1]))
print(mergeTwoArrays([2,5,6], [3,4,8,9]))
print(mergeTwoArrays([1,2,3,3], [4,5,6]))
print(mergeTwoArrays([1,2], [1,2,3,3]))
print(mergeTwoArrays([], []))
print(mergeTwoArrays([1,2,2,3], []))
print(mergeTwoArrays([9,10], [1,2]))
