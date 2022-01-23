def checkSubarraySum(nums, k):
	if len(nums) < 2:
		return False

	sum_arr = 0
	mapper = {}
	mods = []
	for i in range(0, len(nums)):
		sum_arr = (sum_arr % k + nums[i] % k) % k
		mods.append(sum_arr)
		if sum_arr not in mapper:
			mapper[sum_arr] = i

	for i in range(len(nums)-1, -1, -1):
		if mods[i] == 0 and i > 0:
			return True
		if i - mapper[mods[i]] > 1:
			return True
	return False

# print(checkSubarraySum([23,2,4,6,7], 6))
# print(checkSubarraySum([23,2,6,4,7], 6))
# print(checkSubarraySum([23,2,6,4,7], 13))
# print(checkSubarraySum([23,2,4,6,6], 7))
# print(checkSubarraySum([1,0], 2))
# print(checkSubarraySum([0], 1))
# print(checkSubarraySum([5, 0, 0, 0], 3))
print(checkSubarraySum([0,1,0,3,0,4,0,4,0], 5))

	
