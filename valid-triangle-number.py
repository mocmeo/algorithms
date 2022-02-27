# def triangleNumber(nums):
# 	nums = sorted(nums)
# 	n = len(nums)
# 	res = 0

# 	for i in range(n-2):
# 		k = i + 2
# 		if nums[i] != 0:
# 			for j in range(i+1, n-1):
# 				while k < n and nums[i] + nums[j] > nums[k]:
# 					k += 1
# 				res += k-j-1

# 	return res

def triangleNumber(nums):
	nums.sort()
	res = 0
	for i in range(len(nums)-1, 1, -1):
		l = 0
		r = i - 1

		while l < r:
			cur_sum = nums[l] + nums[r]
			if cur_sum > nums[i]:
				res += r - l
				r -= 1
			else:
				l += 1
	return res


print(triangleNumber([2,2,3,4]))
print(triangleNumber([4,2,3,4]))
print(triangleNumber([24,3,82,22,35,84,19]))
print(triangleNumber([0, 0, 0, 7]))
print(triangleNumber([0, 1, 1, 1]))

