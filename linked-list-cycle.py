# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        arr = set({})
        while head != None:
            if head in arr:
                return True
            else:
                arr.add(head)
                head = head.next
        return False
