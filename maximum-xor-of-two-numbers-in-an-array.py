def findMaximumXOR(nums):
	res = 0
	for i in range(len(nums)-1):
		for j in range(1, len(nums)):
			if nums[i] ^ nums[j] > res:
				res = nums[i] ^ nums[j]
				print(nums[i], nums[j])

print(findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
