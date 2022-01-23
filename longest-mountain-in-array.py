def longestMountain(arr):
	left = [0]*len(arr)
	right = [0]*len(arr)
	res = 0

	count = 1
	left[0] = 1
	for i in range(1, len(arr)):
		if arr[i] > arr[i-1]:
			count += 1
			left[i] = count
		else:
			count = 1
			left[i] = 1

	count = 1
	right[-1] = 1
	for i in range(len(arr)-2, -1, -1):
		if arr[i] > arr[i+1]:
			count += 1
			right[i] = count
		else:
			count = 1
			right[i] = 1
	
	for i in range(0, len(arr)):
		if left[i] > 1 and right[i] > 1:
			res = max(res, left[i] + right[i] - 1)
	
	return res

print(longestMountain([2,1,4,7,3,2,5]))
print(longestMountain([2,2,2]))
        