def largestAltitude(gain):
	sum_arr = 0
	res = 0
	for num in gain:
		sum_arr += num
		res = max(res, sum_arr)
	return res

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))
