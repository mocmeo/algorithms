def diStringMatch(s):
	res = []
	large = len(s)
	small = 0
	for ch in s:
		if ch == 'D':
			res.append(large)
			large -= 1
		else:
			res.append(small)
			small += 1

	if s[-1] == 'D':
		res.append(large)
	else:
		res.append(small)
	return res

print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDI"))