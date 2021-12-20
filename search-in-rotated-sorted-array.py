def findPivot(nums):
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
	return res
		
def search(nums, target):
	pivot = findPivot(nums)
	l = pivot
	r = pivot + len(nums) - 1

	while l <= r:
		mid = (l + r) // 2
		t_mid = mid % len(nums)
		if nums[t_mid] == target:
			return t_mid
		if nums[t_mid] > target:
			r = mid - 1
		else:
			l = mid + 1
	return -1

print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))
print(search([3,1], 1))





        