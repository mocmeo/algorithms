def isSubsequence(s, t):
	i = 0
	j = 0
	while i < len(s) and j < len(t):
		if s[i] == t[j]:
			i += 1
			j += 1
		else:
			j += 1
	if i < len(s):
		return False
	return True

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("aaaa", "bbaa"))

