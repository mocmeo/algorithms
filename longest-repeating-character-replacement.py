def characterReplacement(s, k):
	mapper = {}
	i, j = 0, 0
	res = 0
	while i < len(s):
		mapper[s[i]] = mapper.get(s[i], 0) + 1
		curLen = i-j+1
		valid = False
		for ch in range(26):
			if chr(ch+65) in mapper:
				if curLen - mapper[chr(ch+65)] <= k:
					valid = True

		if valid:
			res = max(res, curLen)
			i += 1
		else:
			mapper[s[j]] -= 1
			mapper[s[i]] -= 1
			j += 1
	return res

print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
