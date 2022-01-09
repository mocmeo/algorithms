def find132pattern(nums):
	stack = []
	s2 = float('-inf')
	for num in nums[::-1]:
		if num < s2: return True
		while stack and num > stack[-1]: 
			s2 = stack.pop()
		stack.append(num)
	return False

# print(find132pattern([1,2,3,4]))
# print(find132pattern([3,1,4,2]))
# print(find132pattern([-1,3,2,0]))

# print(find132pattern([3,5,0,3,4]))