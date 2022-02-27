from audioop import reverse


def reverseStr(s, k):
	i = 0
	res = ""
	while i < len(s):
		if len(s) - i >= 2*k:
			res += s[i:i+k][::-1] + s[i+k:i+2*k]
		elif len(s) - i < k:
			res += s[i:][::-1]
		else:
			res += s[i:i+k][::-1] + s[i+k:]
		i += 2*k
	return res

print(reverseStr("a", 2))