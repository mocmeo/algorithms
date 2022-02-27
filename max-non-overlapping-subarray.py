def maxNonOverlapping(nums, target):
	sum_arr = 0
	mapper = {}
	mapper[0] = -1
	res = []
	for i in range(len(nums)):
		sum_arr += nums[i]
		
		if sum_arr - target in mapper:
			if not res or res[-1] <= mapper[sum_arr - target]:
				res.append(i)
		mapper[sum_arr] = i
	return res

print(maxNonOverlapping([1,1,1,1,1], 2))
print(maxNonOverlapping([-1,3,5,1,4,2,-9], 6))
print(maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))
print(maxNonOverlapping([1,3,-3,0,2,3,-2,-2], 4))
		