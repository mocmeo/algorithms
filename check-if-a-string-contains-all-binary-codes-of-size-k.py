def hasAllCodes(s, k):
	mapper = {}
	initStr = s[:k]
	myHash = 0
	k = 0
	for i in range(len(initStr)-1, -1, -1):
		if initStr[i] == '1':
			myHash |= 1 << k
		k += 1

	mapper[myHash] = 1
	for i in range(k, len(s)):
		if myHash & (1 << k-1):
			myHash ^= 1 << (k-1)
		myHash <<= 1
		if s[i] == '1':
			myHash += 1
		
		mapper[myHash] = 1

	for i in range(1 << k):
		if i not in mapper:
			return False

	return True

print(hasAllCodes("00110110", 2))
print(hasAllCodes("0110", 1))
print(hasAllCodes("0110", 2))
print(hasAllCodes("00000000010011101", 4))

