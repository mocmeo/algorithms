def findLUSlength(strs):
	res = -1
	for i in range(len(strs)):
		duplicate = False

		for j in range(len(strs)):
			if i != j and (strs[i] == strs[j] or strs[i] in strs[j]):
				duplicate = True

		if not duplicate:
			res = max(res, len(strs[i]))

	return res

# print(findLUSlength(["aaa","aaa","aa"]))
# print(findLUSlength(["aba","cdc","eae"]))
# print(findLUSlength(["aabbcc", "aabbcc","cb","abc"]))
        