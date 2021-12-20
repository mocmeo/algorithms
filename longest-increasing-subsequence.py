def findGreaterIndex(nums, target):
	low = 0
	high = len(nums)-1;
	while low <= high:
		mid = (low + high) // 2
		if nums[mid] == target:
			return mid
		if nums[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return low

def lengthOfLIS(nums):
	seq = []
	for i in range(len(nums)):
		cur = nums[i]
		if not len(seq) or seq[len(seq)-1] < nums[i]:
			seq.append(nums[i])
		else:
			idx = findGreaterIndex(seq, nums[i])
			seq[idx] = min(seq[idx], nums[i])

	return len(seq)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([0,5,4,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([-1,-2,-3,-4,-5,-6]))
