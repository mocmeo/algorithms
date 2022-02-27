def countTriplets(arr):
	S = []
	xor_arr = 0
	res = 0
	for num in arr:
		xor_arr ^= num
		S.append(xor_arr)

	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			if (i == 0 and S[j] == 0) or (i > 0 and S[i-1]^S[j] == 0):
				res += j-i
	return res

print(countTriplets([2,3,1,6,7]))
print(countTriplets([1,1,1,1,1]))

	