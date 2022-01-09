def removeKdigits(num, k):
	stack = []
	count = k
	for i in range(len(num)):
		while stack and stack[-1] > num[i]:
			if count == 0 or stack[-1] == '0': 
				break
			if stack[-1] > '0':
				stack.pop()
				count -= 1
		stack.append(num[i])

	res = ""
	leadingZero = True
	for i in range(len(stack)-count):
		if leadingZero and stack[i] == '0':
			continue
		else:
			leadingZero = False
			res += stack[i] 

	if not res:
		return "0"
	return res

print(removeKdigits("1432219", 3))
print(removeKdigits("1000035", 2))
print(removeKdigits("10200", 1))
print(removeKdigits("10", 2))
print(removeKdigits("112", 1))
		
		

			