def longestCommonSubsequence(text1, text2):
	n = max(len(text1), len(text2))
	F = [[0]*n for i in range(n)]
	F[0][0] = 1 if text1[0] == text2[0] else 0

	for j in range(1, len(text2)):
		if text1[0] == text2[j]:
			F[0][j] = 1
		else:
			F[0][j] = F[0][j-1]

	for i in range(1, len(text1)):
		if text1[i] == text2[0]:
			F[i][0] = 1
		else:
			F[i][0] = F[i-1][0]

	for i in range(1, len(text1)):
		for j in range(1, len(text2)):
			if text1[i] == text2[j]:
				F[i][j] = max(F[i][j], F[i-1][j-1] + 1)
			else:
				F[i][j] = max(F[i-1][j], F[i][j-1])

	return F[len(text1)-1][len(text2)-1]

print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))
print(longestCommonSubsequence("zacc", "a"))