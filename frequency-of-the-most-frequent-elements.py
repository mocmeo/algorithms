def maxFrequency(nums, k):
	nums.sort()
	left = 0
	sum_arr = 0
	for i in range(len(nums)):
		sum_arr += nums[i]
		if nums[i]*(i-left+1) - sum_arr > k:
			sum_arr -= nums[left]
			left += 1

	return len(nums) - left

print(maxFrequency([1,4,8,13], 5))
print(maxFrequency([1,2,4], 5))
print(maxFrequency([3,9,6], 2))
