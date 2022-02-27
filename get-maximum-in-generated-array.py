def getMaximumGenerated(n):
	if n <= 1:
		return n
	nums = [0,1]
	for x in range(2, n+1):
		i = x // 2
		if x % 2 == 0:
			nums.append(nums[i])
		else:
			nums.append(nums[i] + nums[i+1])
	return max(nums)

print(getMaximumGenerated(7))
print(getMaximumGenerated(2))
print(getMaximumGenerated(3))
print(getMaximumGenerated(1))
		
