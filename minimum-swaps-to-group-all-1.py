def minSwaps(nums):
	len1 = sum(nums)
	t_sum = sum(nums[0:len1])
	res = len1
	for i in range(len1, len(nums)*2):
		res = min(res, len1 - t_sum)
		t_sum += nums[i % len(nums)]
		t_sum -= nums[(i - len1) % len(nums)]

	return res

print(minSwaps([0,1,0,1,1,0,0]))
print(minSwaps([0,1,1,1,0,0,1,1,0]))
print(minSwaps([1,1,0,0,1]))

	