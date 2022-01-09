def genStackLeft(nums):
	arr_id = [0]*len(nums)
	stack = []
	for i in range(len(nums)):
		arr_id[i] = i
		while stack and stack[-1][0] >= nums[i]:
			arr_id[i] = stack[-1][1]
			stack.pop()

		stack.append([nums[i], arr_id[i]])

	return arr_id

def genStackRight(nums):
	arr_id = [0]*len(nums)
	stack = []
	for i in range(len(nums)-1, -1, -1):
		arr_id[i] = i
		while stack and stack[-1][0] >= nums[i]:
			arr_id[i] = stack[-1][1]
			stack.pop()

		stack.append([nums[i], arr_id[i]])

	return arr_id	

def largestRectangleArea(heights):
	res = 0
	left = genStackLeft(heights)
	right = genStackRight(heights)

	for i in range(len(heights)):
		distance = abs(right[i] - left[i]) + 1
		res = max(res, distance*heights[i])
	return res

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([2,4]))
print(largestRectangleArea([1,1]))


		
