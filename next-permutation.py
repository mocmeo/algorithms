
import sys 

def nextPermutation(nums):
	arr_len = len(nums)
	pivot = -1

	for i in range(arr_len-1):
		if nums[i] < nums[i+1]:
			decreasing = True
			for j in range(i+1, arr_len - 1):
				if nums[j] < nums[j+1]:
					decreasing = False
					break
				
			if decreasing:
				pivot = i

	next_larger = sys.maxint
	next_larger_id = 0
	for i in range(pivot + 1, arr_len):
		if nums[i] > nums[pivot] and next_larger >= nums[i]:
			next_larger = nums[i]
			next_larger_id = i

	nums[pivot], nums[next_larger_id] = nums[next_larger_id], nums[pivot]
	for i in range(pivot+1, arr_len-1):
		for j in range(i+1, arr_len):
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]

	return nums

print(nextPermutation([2,3,5,4,7,6]))
print(nextPermutation([1,4,2,3]))
print(nextPermutation([6,3,4,5,2,1]))
print(nextPermutation([3,2,1]))
print(nextPermutation([1,1,5]))
print(nextPermutation([1,5,1]))

print(nextPermutation([1,2]))