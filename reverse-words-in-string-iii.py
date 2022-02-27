def reverseWords(s):
	arr = s.split(" ")
	res = []
	for word in arr:
		res.append(word[::-1])
	return " ".join(res)

print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))
        