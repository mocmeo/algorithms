def findMin(nums):
	l = 0
	r = len(nums)-1
	res = len(nums)
	while l <= r:
			mid = (l + r) // 2
			if nums[mid] >= nums[0]:
					l = mid + 1
			else:
					res = min(res, mid)
					r = mid - 1
	return nums[res%len(nums)]


print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))
print(findMin([2,1]))

