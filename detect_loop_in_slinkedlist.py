
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detect_loop(self, head):
        # using two pointer method
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                print('loop at node {}'.format(slow.val))
                return
        print("No Loop")
        return


# 1 -> 2-> 3-> 4 ->5 -> 2 (existing node 2)

sll_head = ListNode(1)
sll_head.next = ListNode(2)
sll_head.next.next = ListNode(3)
sll_head.next.next  = ListNode(4)
sll_head.next.next.next  = ListNode(5)
sll_head.next.next.next.next  = sll_head.next
Solution().detect_loop(sll_head)