def maxArea(height):
	left = 0
	right = len(height)-1
	res = 0
	while left < right:
		while height[left] > height[right]:
			right -= 1
		res = max(res, (right - left)*height[left])
		left += 1
	
	left = 0
	right = len(height)-1
	while left < right:
		while height[left] < height[right]:
			left += 1
		res = max(res, (right-left)*height[right])
		right -= 1
	return res

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))