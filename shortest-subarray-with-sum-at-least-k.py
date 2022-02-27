def shortestSubarray(nums, k):
	sum_arr = 0
	left = -1
	res = float('inf')

	for i in range(len(nums)):
		sum_arr += nums[i]

		while sum_arr >= k or (nums[left + 1] < 0):
			res = min(res, i - left)
			left += 1
			sum_arr -= 0 if left == -1 else nums[left]

	if res == float('inf'):
		return -1
	return res

print(shortestSubarray([2,-1,2], 3))
print(shortestSubarray([1,2], 4))
print(shortestSubarray([1], 1))
print(shortestSubarray([17,85,93,-45,-21], 150))
print(shortestSubarray([56,-21,56,35,-9], 61))
print(shortestSubarray([84,-37,32,40,95], 167))


