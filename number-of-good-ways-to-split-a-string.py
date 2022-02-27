from collections import Counter

def numSplits(s):
	res = 0
	map1 = {}
	map2 = Counter(s)
	for ch in s:
		map1[ch] = map1.get(ch, 0) + 1
		map2[ch] -= 1
		count1 = 0
		count2 = 0
		for ch in map1.keys():
			if map1[ch]:
				count1 += 1
		for ch in map2.keys():
			if map2[ch]:
				count2 += 1
		if count1 == count2:
			res += 1
	return res

print(numSplits("aacaba"))
print(numSplits("abcd"))