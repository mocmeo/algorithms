from collections import Counter

def wordCount(startWords, targetWords):
	nums = []
	res = 0
	for word in startWords:
		x = 0
		for ch in word:
			x |= 1 << (ord(ch) - ord('a'))
		nums.append(x)
	count = Counter(nums)

	for word in targetWords:
		x = 0
		for ch in word:
			x |= 1 << (ord(ch) - ord('a'))
		for ch in word:
			t_num = x - (1 << (ord(ch) - ord('a')))
			if t_num in count:
				res += 1
				break
	
	return res

print(wordCount(["ant","act","tack"], ["tack","act","acti"]))
print(wordCount(["ab","a"], ["abc","abcd"]))
		

	