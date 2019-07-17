# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        node = head
        while node != None:
            nextNode = node.next
            if nextNode != None and nextNode.val == node.val:
                node.next = nextNode.next
            else:
                node = node.next
        return head
