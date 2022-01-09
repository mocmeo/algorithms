def trap(height):
	left = [0]*len(height)
	right = [0]*len(height)
	left[0] = height[0]
	right[-1] = height[-1]

	res = 0
	for i in range(1, len(height)):
		left[i] = max(left[i-1], height[i])

	for i in range(len(height)-2, -1, -1):
		right[i] = max(right[i+1], height[i])

	for i in range(len(height)):
		res += min(left[i], right[i]) - height[i]

	return res
	
print(trap([4,2,0,3,2,5]))	
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([6,2,0,3,2,5,2,7]))
# print(trap([4,2,3]))
# print(trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
