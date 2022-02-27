def checkWords(s, word):
	i = 0
	j = 0
	while i < len(s) and j < len(word):
		if s[i] == word[j]:
			ch = s[i]
			cntS = 0
			cntWord = 0
			while i < len(s) and s[i] == ch:
				i += 1
				cntS += 1
			while j < len(word) and word[j] == ch:
				j += 1
				cntWord += 1
			if (cntS < 3 and cntS != cntWord) or (cntS < cntWord):
				return 0
		else:
			return 0
		
	if i == len(s) and j == len(word):
		return 1
	else:
		return 0

def expressiveWords(s, words):
	res = 0
	for word in words:
		res += checkWords(s, word)
	return res

print(expressiveWords("heeellooo", ["hello", "hi", "helo"]))
print(expressiveWords("zzzzzyyyyy", ["zzyy","zy","zyy"]))
print(expressiveWords("aaa", ["aaaa"]))
