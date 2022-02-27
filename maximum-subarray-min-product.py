def maxSumMinProduct(nums):
	nums.append(0)
	presum = []
	stack = []
	res = 0
	S = 0

	for num in nums:
		S += num
		presum.append(S)

	for i in range(len(nums)):
		while stack and nums[stack[-1]] > nums[i]:
			idx = stack.pop()

			if stack:
				res = max(res, nums[idx] * (presum[i-1] - presum[stack[-1]]))
			else:
				res = max(res, nums[idx] * presum[i-1])

		stack.append(i)

	return res % (10**9 + 7)

print(maxSumMinProduct([3,1,5,6,4,2]))
print(maxSumMinProduct([1,2,3,2]))
print(maxSumMinProduct([2,3,3,1,2]))
print(maxSumMinProduct([2,5,4,2,4,5,3,1,2,4]))
print(maxSumMinProduct([3,5,3,1,4,5,1,4,1,5]))




			

