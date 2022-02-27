def ordCh(ch):
	return 1 << (ord(ch) - ord('a'))

def wonderfulSubstrings(word):
	mapper = {}
	mapper[0] = 1
	x = 0
	res = 0
	for ch in word:
		x ^= ordCh(ch)

		if x in mapper:
			res += mapper[x]
		for i in range(11):
			xx = 1 << i
			if x ^ xx in mapper:
				res += mapper[x ^ xx]
		mapper[x] = mapper.get(x, 0) + 1
	return res

print(wonderfulSubstrings("aba"))
print(wonderfulSubstrings("aabb"))

