def checkValid(x, n):
	count = 0
	for i in range(n*2):
		if x & (1 << i) == 0:
			count += 1
		else:
			count -= 1
		if count < 0:
			return False

	if count != 0:
		return False
	return True

def generateParenthesis(n):
	res = []
	for i in range(1 << (n*2)):
		if checkValid(i, n):
			pairs = ""
			for j in range(n*2):
				if i & (1 << j) == 0:
					pairs += "("
				else:
					pairs += ")"
			res.append(pairs)

	return res

print(generateParenthesis(1))

