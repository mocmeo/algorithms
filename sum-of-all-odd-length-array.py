def sumOddLengthSubarrays(arr):
	S = []
	sum_arr = 0
	res = 0
	for i in range(len(arr)):
		sum_arr += arr[i]
		S.append(sum_arr)


	for i in range(1, len(arr)+1):
		if i % 2 == 1:
			res += S[i-1]
			for j in range(i, len(arr)):
				res += S[j] - S[j-i]
	return res

print(sumOddLengthSubarrays([1,4,2,5,3]))

		