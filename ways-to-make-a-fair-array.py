def waysToMakeFair(nums):
	even = [0]*len(nums)
	odd = [0]*len(nums)
	if len(nums) % 2 == 0:
		even[-1] = nums[-1]
		odd[-1] = 0
	else:
		even[-1] = 0
		odd[-1] = nums[-1]

	for i in range(len(nums)-2, -1,-1):
		if (i+1) % 2 == 0:
			even[i] = even[i+1] + nums[i]
			odd[i] = odd[i+1]
		else:
			even[i] = even[i+1]
			odd[i] = odd[i+1] + nums[i]

	odd_n = even_n = 0
	res = 0
	for i in range(len(nums)):
		if (i+1) % 2 == 0:
			odd_sum = odd_n + even[i] - nums[i]
			even_sum = even_n + odd[i]
			if odd_sum == even_sum:
				res += 1
			even_n += nums[i]
		else:
			odd_sum = odd_n + even[i]
			even_sum = even_n + odd[i] - nums[i]
			if odd_sum == even_sum:
				res += 1
			odd_n += nums[i]

	return res


print(waysToMakeFair([2,1,6,4]))
print(waysToMakeFair([1,1,1]))
print(waysToMakeFair([1,2,3]))
