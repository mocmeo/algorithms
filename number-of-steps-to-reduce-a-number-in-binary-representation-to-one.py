def numSteps(s):
	arr = []
	for ch in s:
		arr.append(ord(ch) - ord('0'))

	res = 0
	n = len(s)-1
	while n > 0:
		cnt = 0
		i = n
		while i >= 0 and arr[i] == 1:
			arr[i] = 0
			cnt += 1
			i -= 1
		arr[i] = 1
		print(arr)
		while n >= 0 and arr[n] == 0:
			res += 1
			n -= 1
	return res

print(numSteps("1101"))
# print(numSteps("10"))