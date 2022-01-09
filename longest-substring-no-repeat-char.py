def lengthOfLongestSubstring(s):
	mapper = {}
	l = 0
	r = 0
	res = 1
	while r < len(s):
		ch = s[r]
		if ch in mapper and l <= mapper[ch]:
			l = mapper[ch]+1
		mapper[ch] = r

		res = max(res, r-l+1)
		r += 1

	return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("abcdef"))
# print(lengthOfLongestSubstring("abcdefgheaaabbbasdf"))
# print(lengthOfLongestSubstring(""))
# print(lengthOfLongestSubstring("dvdf"))




        