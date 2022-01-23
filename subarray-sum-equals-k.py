def subarraySum(nums, k):
	mapper = {}
	mapper[0] = 1
	sum_arr = 0
	res = 0

	for num in nums:
		sum_arr += num
		if sum_arr - k in mapper:
			res += mapper[sum_arr - k]
		
		if sum_arr in mapper:
			mapper[sum_arr] += 1
		else:
			mapper[sum_arr] = 1
	return res

print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))
print(subarraySum([0, 0], 0))
print(subarraySum([1,0,1,0,1], 2))
print(subarraySum([0,0,0,0,0], 0))

