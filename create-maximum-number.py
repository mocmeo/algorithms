def genNumsKLength(nums, k):
	count = len(nums) - k
	stack = []
	for i in range(len(nums)):
		while stack and stack[-1] < nums[i]:
			if count == 0:
				break
			stack.pop()
			count -= 1
		stack.append(nums[i])

	if count == 0:
		return stack
	return stack[:-count]

def findMax(arr1, arr2, i, j):
	while i < len(arr1) and j < len(arr2):
		if arr1[i] > arr2[j]:
			return True
		elif arr1[i] < arr2[j]:
			return False
		else:
			i += 1
			j += 1
	return i != len(arr1)  # tricky, if i < len(arr1) => j == arr2 alrdy => pick i

def mergeArrays(arr1, arr2, k):
	merger = []
	i = 0
	j = 0
	idx = 0
	while idx < k:
		if findMax(arr1, arr2, i, j):
			merger.append(arr1[i])
			i += 1
		else:
			merger.append(arr2[j])
			j += 1
		idx += 1
	
	return merger


def maxNumber(nums1, nums2, k):
	maxRes = [0]*k
	for i in range(k+1):
		if i <= len(nums1) and k-i <= len(nums2):
			s1 = genNumsKLength(nums1, i)
			s2 = genNumsKLength(nums2, k-i)
			merged = mergeArrays(s1, s2, k)
			compareRes = findMax(merged, maxRes, 0, 0)
			if compareRes:
				maxRes = merged
	return maxRes

print(maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))
print(maxNumber([6,7], [6,0,4], 5))
print(maxNumber([3,9], [8,9], 3))
print(maxNumber([5,6,8], [6,4,0], 3))
print(maxNumber([3,4,8,9,3,0], [6,1,9,1,1,2], 6))
print(maxNumber([5, 1, 0], [5,2,1], 3))
print(maxNumber([6,5,4,6,3,7,5,6,4,5,6,4], [8,8,6,0], 16))




  