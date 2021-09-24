def rotate(nums, k):
	arr_len = len(nums)
	seg_len = k % len(nums)
	for i in range(len(nums)/2):
		nums[i], nums[arr_len - i - 1] = nums[arr_len - i - 1], nums[i]

	for i in range(seg_len/2):
		nums[i], nums[seg_len - i - 1] = nums[seg_len - i - 1], nums[i]

	for i in range((arr_len - seg_len)/2):
		nums[seg_len + i], nums[arr_len - i - 1] = nums[arr_len - i - 1], nums[seg_len + i]
	
	return nums

print(rotate([1, 2, 3, 4, 5, 6,7,8,9,10,11,12], 2))
