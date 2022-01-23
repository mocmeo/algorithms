def pivotIndex(nums):
	sum_arr = sum(nums)
	x = 0
	for i in range(len(nums)):
		x += nums[i]
		if sum_arr - x == x - nums[i]:
			return i
	return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))