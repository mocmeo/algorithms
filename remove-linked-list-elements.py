# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        my_head = p = ListNode(0)
        p.next = head

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return my_head.next
