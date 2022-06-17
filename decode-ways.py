def numDecodings(s):
	mapper = {}
	for i in range(26):
		mapper[str(i+1)] = 1

	arr = [0] * (len(s))
	newS = ""
	for i in range(len(s)):
		newS += s[i]

		if len(newS) >= 2:
			if newS[-2:] in mapper:
				if len(newS) == 2:
					arr[i] += 1
				else:
					arr[i] += arr[i-2]
		if len(newS) >= 1:
			if newS[-1] in mapper:
				if len(newS) == 1:
					arr[i] += 1
				else:
					arr[i] += arr[i-1]
	return arr[-1]
			
print(numDecodings("12"))
	

	
