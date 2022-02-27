def sortColors(nums):
	j = 0
	for i in range(len(nums)):
		if nums[i] == 0:
			nums[i], nums[j] = nums[j], nums[i]
			j += 1

	for i in range(len(nums)):
		if nums[i] == 1:
			nums[i], nums[j] = nums[j], nums[i]
			j += 1
	return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))