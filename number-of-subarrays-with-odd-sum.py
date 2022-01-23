def numOfSubarrays(arr):
	modulo = pow(10, 9) + 7
	sum_arr = 0
	odd = 0
	even = 1
	res = 0
	for num in arr:
		sum_arr += num
		if sum_arr % 2 == 0:
			res = (res % modulo + odd % modulo) % modulo
			even += 1
		else:
			res = (res % modulo + even % modulo) % modulo
			odd += 1
	return res

print(numOfSubarrays([1,3,5]))
print(numOfSubarrays([2,4,6]))
print(numOfSubarrays([1,2,3,4,5,6,7]))
		
		