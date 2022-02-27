def singleNumber(nums):
	min_num = min(nums)
	if min_num < 0:
		min_num = -min_num

	for i in range(len(nums)):
		nums[i] += min_num
		
	res = 0
	for i in range(64):
		count = 0
		for num in nums:
			mask = 1 << i
			if num & mask > 0:
				count += 1
		if count % 3 != 0:
			res |= 1 << i

	return res - min_num

print(singleNumber([2,2,3,2]))
print(singleNumber([0,1,0,1,0,1,99]))
print(singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))


