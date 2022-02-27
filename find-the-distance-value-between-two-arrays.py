def findTheDistanceValue(arr1, arr2, d):
	res = 0
	for num in arr1:
		min_dist = float('inf')
		for i in range(len(arr2)):
			min_dist = min(min_dist, abs(num - arr2[i]))
		if min_dist > d:
			res += 1

	return res

print(findTheDistanceValue([4,5,8], [10,9,1,8], 2))
print(findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3))
print(findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6))
