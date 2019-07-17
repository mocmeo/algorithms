# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        arr = []
        node = head
        while node != None:
            arr.append(node)
            node = node.next

        n = len(arr)
        return arr[int(n/2)]
