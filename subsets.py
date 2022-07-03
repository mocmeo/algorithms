def subsets(nums):
	arr = [[]]
	for num in nums:
		temp = []
		for cur in arr:
			x = cur + [num]
			temp.append(x)
		arr += temp
	return arr

print(subsets([1,2,2]))
# n = 3
# nth_bit = 1 << n
# for i in range(2**n):
# 	# generate bitmask, from 0..00 to 1..11
# 	bitmask = bin(i | nth_bit)[3:]
# 	print(bitmask)