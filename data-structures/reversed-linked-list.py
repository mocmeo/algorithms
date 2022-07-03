class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(l):
    prev = next = None
    cur = l
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(reverseLinkedList(head))