# def countSubarrayUnderbound(nums, limit):
# 	inc = 0
# 	count = 0
# 	for num in nums:
# 		if num <= limit:
# 			inc += 1
# 			count += inc
# 		else:
# 			inc = 0
# 	return count

# def numSubarrayBoundedMax(nums, left, right):
# 	return countSubarrayUnderbound(nums, right) - countSubarrayUnderbound(nums, left - 1)

# def numSubarrayBoundedMax(nums, left, right):
# 	j, k = -1, -1
# 	count = 0

# 	for i in range(len(nums)):
# 		if nums[i] > right:
# 			k = i
# 		if nums[i] >= left:
# 			j = i
# 		count += j-k
# 	return count

def numSubarrayBoundedMax(nums, left, right):
	start, window_len, count = 0, 0, 0
	for i, val in enumerate(nums):
		if left <= val <= right:
			window_len = i - start + 1
		elif val > right:
			window_len = 0
			start = i + 1
		count += window_len
	return count


print(numSubarrayBoundedMax([2,1,4,3], 2, 3))
print(numSubarrayBoundedMax([2,9,2,5,6], 2, 8))
