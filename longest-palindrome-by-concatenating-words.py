from collections import Counter

def longestPalindrome(words):
	res = 0
	count = Counter(words)
	seen = set([])

	hasOdd = False

	for word in count:
		if word[0] == word[-1]:
			if count[word] % 2 == 0:
				res += count[word]*2
			else:
				hasOdd = True
				res += (count[word]-1)*2
	if hasOdd:
		res += 2

	for word in count:
		if word in seen or word[::-1] in seen:
			continue
		if word[0] == word[-1]:
			continue
		else:
			r_word = word[::-1]
			res += min(count[word], count[r_word])*4
			seen.add(word)
			seen.add(r_word)
	return res

print(longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
print(longestPalindrome(["lc","cl","gg"]))
print(longestPalindrome(["cc","ll","xx"]))
print(longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
