def subarraysDivByK(nums, k):
	mapper = {}
	mapper[0] = 1
	res = 0
	sum_arr = 0
	for num in nums:
		sum_arr += num
		modulo = sum_arr % k

		if modulo in mapper:
			res += mapper[modulo]
		
		mapper[modulo] = mapper.get(modulo, 0) + 1
	return res

print(subarraysDivByK([4,5,0,-2,-3,1], 5))
print(subarraysDivByK([5], 9))
