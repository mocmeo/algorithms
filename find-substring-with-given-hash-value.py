def ordCh(ch):
	return ord(ch) - ord('a') + 1

def subStrHash(s, power, modulo, k, hashValue):
	pk = 1
	first = float('inf')
	for _ in range(k-1):
		pk = pk * power % modulo

	myHash = 0
	temp = 1
	for i in range(len(s)-k, len(s)):
		myHash = (myHash + ordCh(s[i]) * temp % modulo) % modulo
		temp = temp * power % modulo

	if myHash == hashValue:
		first = len(s) - k

	for i in range(len(s)-k-1, -1, -1):
		myHash = (myHash - ordCh(s[i+k])*pk % modulo) % modulo
		myHash = (myHash * power % modulo) % modulo
		myHash = (myHash + ordCh(s[i])) % modulo

		if myHash == hashValue:
			first = i

	return s[first:first+k]

print(subStrHash("leetcode", 7, 20, 2, 0))
print(subStrHash("fbxzaad", 31, 100, 3, 76))
print(subStrHash("dlojuxgftvpqpsknfgkejydsxgcgyroavsefjrejytcgflrnnxxsxowqbteycujnrbaokjibq", 8, 54, 30, 16))


