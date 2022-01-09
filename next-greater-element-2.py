def genStack(nums):
	res = [0]*len(nums)
	stack = []
	for i in range(len(nums)-1,-1,-1):
		while stack and stack[-1] <= nums[i]:
			stack.pop()
		if not stack:
			res[i] = -1
		else:
			res[i] = stack[-1]
		stack.append(nums[i])
	return res


def nextGreaterElements(nums):
	ans = genStack(nums+nums)

	return ans[:len(nums)]

# print(nextGreaterElements([1,2,3,4,3]))
# print(nextGreaterElements([1,2,1]))
# print(nextGreaterElements([5,4,3,2,1]))
		
