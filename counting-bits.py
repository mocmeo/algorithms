def countBits(n):
	nums = [0]
	for i in range(1, n+1):
		nums.append((i&1) + nums[i >> 1])
	return nums

print(countBits(5))
				

	

	