def checkValid(m1, m2, myset):
	for ch in myset:
		if m1.get(ch, 0) < m2.get(ch, 0):
				return False
	return True


def minWindow(s, t):
	mapper = {}
	myset = set()
	for ch in t:
		mapper[ch] = mapper.get(ch, 0) + 1
		myset.add(ch)

	mapper1 = {}
	i = 0
	j = 0
	res = len(s)+1
	ans = ""
	while j < len(s):
		mapper1[s[j]] = mapper1.get(s[j], 0) + 1
		j += 1
		while checkValid(mapper1, mapper, myset):
			if j-i < res:
				res = j-i
				ans = s[i:j]

			mapper1[s[i]] -= 1
			i += 1
	return ans
	
print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
