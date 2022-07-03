def setZeroes(matrix):
	first_row = False
	first_col = False
	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			first_col = True
			break

	for j in range(len(matrix[0])):
		if matrix[0][j] == 0:
			first_row = True
			break

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0

	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			if matrix[i][0] == 0 or matrix[0][j] == 0:
				matrix[i][j] = 0

	if first_col:
		for i in range(len(matrix)):
			matrix[i][0] = 0

	if first_row:
		for j in range(len(matrix[0])):
			matrix[0][j] = 0

	return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))