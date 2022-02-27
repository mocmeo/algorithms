def countSubstrings(s, t):
	res = 0
	for i in range(len(s)):
		for j in range(len(t)):
			p, q = i, j
			count = 0
			while p >= 0 and q >= 0:
				if s[p] != t[q]:
					count += 1
				if count == 1:
					res += 1
				if count > 1:
					break
				p -= 1
				q -= 1
			
	return res

print(countSubstrings("aba", "baba"))
print(countSubstrings("ab", "bb"))
print(countSubstrings("abe", "bbc"))
print(countSubstrings("abbab", "bbbbb"))