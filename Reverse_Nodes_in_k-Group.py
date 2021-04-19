# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

def reverseKGroup(head, k):
    def reverseLL(head, k):
        prev, curr = None, head
        while curr and k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1
        return prev

    newhead = None
    ktail = None
    ptr = head

    while ptr:
        count = 0
        ptr = head

        while ptr and count < k:
            ptr = ptr.next
            count += 1
        if count == k:
            revhead = reverseLL(head, k)
            if not newhead:
                newhead = revhead
            if ktail:
                ktail.next = revhead

            ktail = head
            head = ptr
    if ktail:
        ktail.next = head

    return newhead if newhead else None

