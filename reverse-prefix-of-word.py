def reversePrefix(word, ch):
	pos = -1
	for i in range(len(word)):
		if pos == -1 and word[i] == ch:
			pos = i

	if pos > -1:
		subst = word[:pos+1][::-1]
		return subst + word[pos+1:]
	return word

print(reversePrefix("abcd", "c"))
print(reversePrefix("abcdefd", "d"))
print(reversePrefix("xyxzxe", "z"))
print(reversePrefix("abcd", "z"))