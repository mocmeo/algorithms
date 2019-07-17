# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        nextNode = node.next
        if nextNode is None:
            node = nextNode
        else:
            node.val = nextNode.val
            node.next = nextNode.next
