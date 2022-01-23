def getSumAbsoluteDifferences(nums):
	S = []
	res = [0]*len(nums)
	sum_arr = 0
	for num in nums:
		sum_arr += num
		S.append(sum_arr)

	for i in range(0, len(nums)):
		if i == 0:
			res[i] = S[-1] - nums[0]*len(nums)
		elif i == len(nums)-1:
			res[i] = nums[-1]*len(nums) - S[-1]
		else:
			res[i] = (nums[i]*i - S[i-1]) + (S[-1] - S[i] - nums[i]*(len(nums)-i-1))
	return res

print(getSumAbsoluteDifferences([2,3,5]))
print(getSumAbsoluteDifferences([1,4,6,8,10]))
print(getSumAbsoluteDifferences([1]))

	