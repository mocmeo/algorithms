import collections

def maxSlidingWindow(nums, k):
	stack = collections.deque([])
	res = []

	for i in range(len(nums)):
		while stack and nums[stack[-1]] < nums[i]:
			stack.pop()
		
		if i >= k - 1:
			if stack and stack[0] < i - k + 1:
					stack.popleft()
			if not stack:
				res.append(nums[i])
			else:
				res.append(nums[stack[0]])
		stack.append(i)
	return res
		

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1, -1], 1))



