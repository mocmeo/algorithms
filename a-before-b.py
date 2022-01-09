def checkString(s):
	aId = -1
	bId = -1
	for i in range(len(s)):
		if s[i] == 'a':
			aId = i
		if s[i] == 'b' and bId == -1:
			bId = i
	if aId == -1 or bId == -1:
		return True
	if aId < bId:
		return True
	return False

# print(checkString("aaabbb"))
# print(checkString("abab"))
# print(checkString("bbb"))
print(checkString("a"))

        