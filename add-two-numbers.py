class ListNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def addTwoNumbers(l1, l2):
	carry = 0
	head = p = ListNode(0)
	while l1 or l2:
		x = y = 0
		if l1: x = l1.val
		if l2: y = l2.val
		mysum = x + y + carry
		p.next = mysum % 10
		p = p.next
		carry = mysum // 10
		if l1: l1 = l1.next
		if l2: l2 = l2.next

	if carry: 
		p.next = carry
	return head.next
		

l1 = ListNode(2)
l11 = ListNode(4)
l111 = ListNode(3)
l11.next = l111
l1.next = l11

l2 = ListNode(5)
l22 = ListNode(6)
l222 = ListNode(8)
l22.next = l222
l2.next = l22

print(addTwoNumbers(l1, l2))
