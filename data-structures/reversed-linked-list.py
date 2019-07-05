# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def reverse(self):
        prev = None
        next = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


class Solution(object):
    def reverseList(self, head):
        myLL = LinkedList(head)
        myLL.reverse()
        return myLL.head
