def jump(nums):
	x = 0
	F = [len(nums)+1]*len(nums)
	F[0] = 0
	for i in range(1, len(nums)):
		while x + nums[x] < i:
			x += 1
		F[i] = min(F[i], F[x]+1)
	return F[-1]

# print(jump([2,3,1,1,4]))
# print(jump([2,3,0,1,4]))

