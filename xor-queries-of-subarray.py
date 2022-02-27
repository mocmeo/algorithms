def xorQueries(arr, queries):
	S = []
	res = []
	xor_arr = 0
	for num in arr:
		xor_arr ^= num
		S.append(xor_arr)

	for q in queries:
		if q[0] == 0:
			res.append(S[q[1]])
		else:
			res.append(S[q[1]] ^ S[q[0] - 1])
	return res

print(xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
print(xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))
		