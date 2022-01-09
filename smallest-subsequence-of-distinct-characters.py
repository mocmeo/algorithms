def smallestSubsequence(s):
	seen = {el: index for index, el in enumerate(s)}
	ans = []

	for i in range(len(s)):
		if s[i] in set(ans):
			continue
		while len(ans) > 0: 
			top = ans[-1]
			if top > s[i] and seen[top] > i:
				ans.pop()
			else:
				break
		ans.append(s[i])
		
	return "".join(ans)

print(smallestSubsequence("cbacdcbc"))
# print(smallestSubsequence("bcabc"))
# print(smallestSubsequence("adcabdccabdeabdeabecde"))
# print(smallestSubsequence("cbaacabcaaccaacababa"))
# print(smallestSubsequence(""))