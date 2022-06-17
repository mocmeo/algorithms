def findTheDifference(s, t):
	s += t
	xor_ch = 0
	for ch in s:
		xor_ch ^= ord(ch)
	return chr(xor_ch)

print(findTheDifference("abcd", "abcde"))
print(findTheDifference("", "y"))