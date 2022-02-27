def rangeSum(nums, n, left, right):
	mapper = {}
	max_num = 0
	count = 0
	res = 0
	modulo = 10**9 + 7

	for i in range(n):
		cur_sum = 0

		for j in range(i, n):
			cur_sum += nums[j]
			max_num = max(max_num, cur_sum)
			mapper[cur_sum] = mapper.get(cur_sum, 0) + 1

	for i in range(1, max_num+1):
		if i in mapper:
			for j in range(mapper[i]):
				count += 1
				if left <= count <= right:
					res = (res + i) % modulo
				if count >= right:
					break

	return res

print(rangeSum([1,2,3,4], 4, 1, 5))
print(rangeSum([1,2,3,4], 4, 3, 4))
print(rangeSum([1,2,3,4], 4, 1, 10))

	

