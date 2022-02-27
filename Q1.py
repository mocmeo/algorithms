def countPairs(nums, k):
	res = 0
	for i in range(len(nums)-1):
		for j in range(i+1, len(nums)):
			if nums[i] == nums[j] and i * j % k == 0:
				res += 1
	return res

print(countPairs([3,1,2,2,2,1,3], 2))
print(countPairs([1,2,3,4], 1))
