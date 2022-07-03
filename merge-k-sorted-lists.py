class ListNode(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def mergeKLists(lists):
	nodes = []
	head = pointer = ListNode(0)
	for l in lists:
		while l:
			nodes.append(l.val)
			l = l.next

	for item in sorted(nodes):
		pointer.next = ListNode(item)
		pointer = pointer.next
	
	return head.next

def printLL(pointer):
	while pointer:
		print(pointer.val)
		pointer = pointer.next

t = ListNode(1)
t1 = ListNode(3)
t2 = ListNode(5)
t.next = t1
t1.next = t2


m = ListNode(2)
m1 = ListNode(4)
m2 = ListNode(6)
m.next = m1
m1.next = m2
printLL(mergeKLists([t, m]))
