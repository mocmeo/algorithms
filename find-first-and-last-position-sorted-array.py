def findFirst(nums, target):
	l = 0
	r = len(nums)-1
	res = len(nums)+1
	while l <= r:
		mid = (l + r) // 2
		if nums[mid] > target:
			r = mid - 1
		if nums[mid] < target:
			l = mid + 1
		if nums[mid] == target:
			r = mid - 1
			res = min(res, mid)

	if res > len(nums): 
		return -1
	return res

def findLast(nums, target):
	l = 0
	r = len(nums)-1
	res = -1
	while l <= r:
		mid = (l + r) // 2
		if nums[mid] > target:
			r = mid - 1
		if nums[mid] < target:
			l = mid + 1
		if nums[mid] == target:
			l = mid + 1
			res = max(res, mid)
	return res

def searchRange(nums, target):
	first = findFirst(nums, target)
	last = findLast(nums, target)
	return [first, last]

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([], 0))
	



	