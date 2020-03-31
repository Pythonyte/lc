# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Get first elements of every list and put into heap
        Each element of heap would be (val, index, node)
            Because while poping, heap have to shiftup and needs to check smallest child
            in case of val are same for both child, it will go for next thing.. which would be index (an int, acceptable for > and <)
            But if we do not add index, then next thing would be ListNode which throws not accepted "<" 
        """
        heap = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapq.heapify(heap)
        output = head = ListNode("Dummy")
        
        while heap:
            val, index, node = heapq.heappop(heap)
            output.next = node
            output = output.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
                
        return head.next
