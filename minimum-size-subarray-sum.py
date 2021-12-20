def minSubArrayLen(target, nums):
	if sum(nums) < target:
		return 0

	left = 0
	sum_arr = 0
	res = len(nums)+1

	for i in range(len(nums)):
		sum_arr += nums[i]
		if sum_arr >= target:
			while sum_arr >= target:
				res = min(res, i-left+1)
				sum_arr -= nums[left]
				left += 1

	return res

print(minSubArrayLen(7, [2,3,1,2,4,2]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
		




        