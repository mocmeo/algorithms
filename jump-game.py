def canJump(nums):
	stack = []
	stack.append(0)
	F = [False]*len(nums)
	F[0] = True

	for i in range(1, len(nums)):
		while stack and nums[stack[-1]] < i - stack[-1]:
			stack.pop()
		if not stack:
			F[i] = False
		else:
			F[i] = True
			stack.append(i)
	return F[-1]

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))

        