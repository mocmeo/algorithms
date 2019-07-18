# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]
