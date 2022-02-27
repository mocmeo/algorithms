def longestOnes(nums, k):
	left = -1
	res = 0
	sum_arr = 0
	for i in range(len(nums)):
		sum_arr += nums[i]
		length = i - left
		if length - sum_arr > k:
			left += 1
			sum_arr -= nums[left]
		else:
			res = max(res, length)
	return res

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))