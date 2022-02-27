def maxScoreIndices(nums):
	sum0, sum1 = 0, 0
	presum0, presum1 = [], []
	max_div = 0
	for num in nums:
		if num == 0:
			sum0 += 1
		else:
			sum1 += 1
		presum0.append(sum0)
		presum1.append(sum1)

	for i in range(len(nums)+1):
		if i == 0:
			max_div = max(max_div, presum1[-1])
		elif i == len(nums):
			max_div = max(max_div, presum0[-1])
		else:
			max_div = max(max_div, presum0[i-1] + (presum1[-1] - presum1[i-1]))

	res = []
	for i in range(len(nums)+1):
		if i == 0:
			if max_div == presum1[-1]:
				res.append(i)
		elif i == len(nums):
			if max_div == presum0[-1]:
				res.append(i)
		else:
			if max_div == presum0[i-1] + presum1[-1] - presum1[i-1]:
				res.append(i)
	return res

print(maxScoreIndices([0,0,1,0]))
print(maxScoreIndices([0,0,0]))
print(maxScoreIndices([1,1]))