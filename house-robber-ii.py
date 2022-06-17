def rob(nums):
	if len(nums) <= 3:
		return max(nums)

	# case 1
	res = 0
	arr = [0]*len(nums)
	arr[0] = nums[0]
	for i in range(1, len(nums)-1):
		if i >= 2:
			arr[i] = max(arr[i-1], arr[i-2] + nums[i])
		else:
			arr[i] = max(arr[i-1], nums[i])
		res = max(res, arr[i])

	# case 2
	arr2 = [0]*len(nums)
	arr2[0] = 0
	arr2[1] = nums[1]
	for i in range(2, len(nums)):
		arr2[i] = max(arr2[i-1], arr2[i-2] + nums[i])
		res = max(res, arr2[i])
	return res

# print(rob([2,3,2]))
# print(rob([1,2,3,1]))
# print(rob([1,2,3]))

print(rob([1,2]))



