def dailyTemperatures(temperatures):
	stack = []
	res = [0]*len(temperatures)
	
	for i in range(len(temperatures)-1, -1,-1):
		while stack and temperatures[stack[-1]] <= temperatures[i]:
			stack.pop()
		if not stack:
			res[i] = 0
		else:
			res[i] = stack[-1] - i
		stack.append(i)
	return res

# print(dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(dailyTemperatures([30,40,50,60]))
# print(dailyTemperatures([30,60,90]))
# print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))