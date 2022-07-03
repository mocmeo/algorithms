class ListNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def reverseBetween(head, left, right):
	arr = []
	while head:
		arr.append(head.val)
		head = head.next
	for i in range((right-left)//2 + 1):
		x = left-1+i
		y = right-1-i
		arr[x], arr[y] = arr[y], arr[x]

	head = p = ListNode(0)
	for num in arr:
		p.next = ListNode(num)
		p = p.next
	return head.next
		

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(reverseBetween(head, 2, 4))
