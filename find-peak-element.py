def findPeakElement(nums):
	if len(nums) == 1:
		return nums[0]
	l, r = 0, len(nums)-1
	while l <= r:
		mid = (l+r)//2
		if mid == 0 and nums[mid] > nums[mid+1]:
			return mid
		if mid == len(nums)-1 and nums[mid] > nums[mid-1]:
			return mid
		if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
			return mid

		if nums[mid] <= nums[mid+1]:
			l = mid+1
		else:
			r = mid-1
	return 0

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))