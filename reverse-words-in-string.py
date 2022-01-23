def reverseWords(s):
	words = s.strip().split(" ")
	stripedWords = []
	for word in words:
		if len(word):
			stripedWords.append(word.strip())

	return " ".join(stripedWords[::-1])

print(reverseWords("a good   example"))