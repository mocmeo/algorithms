def pivotArray(nums, pivot):
	less = []
	more = []
	equal = []
	for num in nums:
		if num < pivot: less.append(num)
		if num > pivot: more.append(num)
		if num == pivot: equal.append(num)
	less.extend(equal)
	less.extend(more)
	return less

print(pivotArray([9,12,5,10,14,3,10], 10))
print(pivotArray([-3,4,3,2], 2)) 