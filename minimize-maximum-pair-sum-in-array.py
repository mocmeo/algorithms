def minPairSum(nums):
	nums = sorted(nums)
	res = float('-inf')

	for i in range(len(nums)/2):
		res = max(res, nums[i] + nums[len(nums)-i-1])

	return res

print(minPairSum([3,5,2,3]))
print(minPairSum([3,5,4,2,4,6]))
