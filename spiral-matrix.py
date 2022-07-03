def spiralOrder(matrix):
	topr = len(matrix[0])
	botr = len(matrix)
	botl = 0
	topl = 0
	res = []
	total = len(matrix) * len(matrix[0])
	while True:
		for j in range(topl, topr): 
			res.append(matrix[topl][j])
			if len(res) == total: return res
		topr -= 1
		topl += 1
		for i in range(topl, botr): 
			res.append(matrix[i][j])
			if len(res) == total: return res
		botr -= 1
		print(botr)
		for j in range(botr, botl-1, -1): 
			res.append(matrix[i][j])
			if len(res) == total: return res
		curI = i
		for i in range(curI-1, topl-1, -1): 
			res.append(matrix[i][j])
			if len(res) == total: return res

# print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
