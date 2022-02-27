def minimumAbsDifference(arr):
	min_sum = float('inf')
	arr = sorted(arr)
	res = []
	for i in range(len(arr)-1):
		min_sum = min(min_sum, abs(arr[i] - arr[i+1]))

	for i in range(len(arr)-1):
		cur_sum = abs(arr[i] - arr[i+1])
		if cur_sum == min_sum:
			res.append([arr[i], arr[i+1]])

	return res

print(minimumAbsDifference([4,2,1,3]))
print(minimumAbsDifference([1,3,6,10,15]))
print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))