from xmlrpc.client import MAXINT


def minStartValue(nums):
	sum_arr = 0
	min_val = float('inf')
	for num in nums:
		sum_arr += num
		min_val = min(min_val, sum_arr)
	
	if min_val >= 0:
		return 1
	else:
		return -min_val + 1

print(minStartValue([-3,2,-3,4,2]))
print(minStartValue([1,2]))
print(minStartValue([0]))