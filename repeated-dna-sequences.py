def findRepeatedDnaSequences(s):
	if len(s) < 10:
		return [s]
	mapper = {}
	count = {}
	res = []
	ords = {"A": 1, "C": 2, "G": 3, "T": 4}
	x = 1
	init = 0
	for i in range(9, -1, -1):
		init += ords[s[i]] * x
		x *= 4

	mapper[init] = s[:10]
	count[init] = 1
	k = init
	for i in range(10, len(s)):
		k -= ords[s[i-10]]*pow(4, 9)
		k *= 4
		k += ords[s[i]]
		mapper[k] = s[i-9:i+1]
		count[k] = count.get(k, 0) + 1

	for key in count:
		if count[key] > 1:
			res.append(mapper[key])
	
	return res

print(findRepeatedDnaSequences("AAAA"))

