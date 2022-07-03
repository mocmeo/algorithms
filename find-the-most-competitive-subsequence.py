def mostCompetitive(nums, k):
	stack = []
	for i in range(len(nums)):
		while stack and nums[i] < stack[-1] and len(stack) + len(nums)-i > k:
			stack.pop()
		stack.append(nums[i])

	return stack[:k]

print(mostCompetitive([7,9,5,2,1,4,3], 4))
print(mostCompetitive([8,5,2,4,7,1], 2))
print(mostCompetitive([3,5,2,6], 2))
print(mostCompetitive([2,4,3,3,5,4,9,6], 4))
		