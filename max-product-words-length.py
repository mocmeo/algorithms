def maxProduct(words):
	res = []
	for word in words:
		mask = 0
		for ch in word:
			mask |= 1 << (ord(ch) - ord('a'))
		res.append([mask, len(word)])

	max_len = 0
	for i in range(len(res) - 1):
		for j in range(i+1, len(res)):
			if not (res[i][0] & res[j][0]):
				max_len = max(max_len, res[i][1] * res[j][1])
	return max_len

print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))