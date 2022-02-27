def xorNum(num, maxBit):
	curXor = 0
	for i in range(maxBit):
		if num & (1 << i) == 0:
			curXor ^= 1 << i
	return curXor

def getMaximumXor(nums, maximumBit):
	S = []
	res = []
	xor_arr = 0
	length = len(nums)

	for num in nums:
		xor_arr ^= num
		S.append(xor_arr)

	for i in range(length):
		res.append(xorNum(S[length-i-1], maximumBit))
	return res

print(getMaximumXor([0,1,1,3], 2))
print(getMaximumXor([2,3,4,7], 3))
print(getMaximumXor([0,1,2,2,5,7], 3))
	

	
