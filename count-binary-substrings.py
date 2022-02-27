def countBinarySubstrings(s):
	num0 = 0
	num1 = 0
	res = 0
	if s[0] == '0':
		num0 += 1
	else:
		num1 += 1

	for i in range(1, len(s)):
		# reset state
		if s[i] == s[i-1]:
			if s[i] == '0':
				num0 += 1
				if num0 <= num1:
					res += 1
			else:
				num1 += 1
				if num1 <= num0:
					res += 1
			
		if s[i] != s[i-1]:
			if s[i] == '0':
				num0 = 1
				res += 1
			else:
				num1 = 1
				res += 1

	return res

print(countBinarySubstrings("00110011"))
print(countBinarySubstrings("10101"))
		

