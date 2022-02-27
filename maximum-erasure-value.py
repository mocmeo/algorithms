def hasItem(mapper, val):
	if val not in mapper:
		return False
	if val in mapper and mapper[val] == -1:
		return False
	return True

def maximumUniqueSubarray(nums):
	presum = []
	sum_arr = 0
	mapper = {}
	for num in nums:
		sum_arr += num
		presum.append(sum_arr)

	left = -1
	res = 0
	nums.append(nums[-1])
	for i in range(len(nums)):
		if not hasItem(mapper, nums[i]):
			mapper[nums[i]] = i
		else:
			if left == -1:
				res = max(res, presum[i-1])
			else:
				res = max(res, presum[i-1] - presum[left])
			
			# update left idx
			idx = mapper[nums[i]]
			while left < idx:
				left += 1
				mapper[nums[left]] = -1
			mapper[nums[i]] = i

	return res

print(maximumUniqueSubarray([4,2,4,5,6]))
print(maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
print(maximumUniqueSubarray([1,2,3]))
		



