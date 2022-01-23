def findTheLongestSubstring(s):
	mapper = {}
	mapper[0] = -1
	bit = 0
	res = 0
	for i in range(len(s)):
		if s[i] in "ueoai":
			bit ^= 1 << (ord(s[i]) - ord('a'))
			if bit not in mapper:
				mapper[bit] = i
		if bit in mapper and mapper[bit] < i:
			res = max(res, i - mapper[bit])

	return res

print(findTheLongestSubstring("eleetminicoworoep"))
# print(findTheLongestSubstring("leetcodeisgreat"))
# print(findTheLongestSubstring("bcbcbc"))

