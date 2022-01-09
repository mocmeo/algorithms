class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head):
	nums = []
	res = 0
	while head:
		nums.append(head.val)
		head = head.next
	for i in range(len(nums)/2):
		res = max(res, nums[i] + nums[len(nums)-i-1])
	return res

        
head = ListNode(5, None)
head1 = ListNode(4, None)
head2 = ListNode(2, None)
head3 = ListNode(1, None)

head.next = head1
head1.next = head2
head2.next = head3

print(pairSum(head))