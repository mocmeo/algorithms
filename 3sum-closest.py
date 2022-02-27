def threeSumClosest(nums, target):
	nums.sort()
	max_diff = float('inf')
	res = 0

	for k in range(len(nums)-1, 1, -1):
		i = 0
		j = k - 1
		while i < j:
			cur_sum = nums[i] + nums[j] + nums[k]
			if cur_sum > target:
				j -= 1
			elif cur_sum < target:
				i += 1
			else:
				return target
			if abs(cur_sum - target) < max_diff:
				max_diff = abs(cur_sum - target)
				res = cur_sum
	return res

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], 1))
		
