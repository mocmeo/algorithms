def maximalRectangle(matrix):
	arr = [0]*(len(matrix[0]) + 1)
	res = 0

	for i in range(len(matrix)):
		stack = []
		
		for j in range(len(matrix[0])):
			if i == 0:
				arr[j] = int(matrix[i][j])
			else:
				if matrix[i-1][j] == "0" or matrix[i][j] == "0":
					arr[j] = int(matrix[i][j])
				else:
					arr[j] = arr[j] + int(matrix[i][j])
		
		for j in range(len(arr)):
			v = arr[j]
			while stack and arr[stack[-1]] > v:
				height = arr[stack.pop()]
				if stack:
					length = j - stack[-1] - 1
				else:
					length = j 
				res = max(res, height * length)
			stack.append(j)
			
	return res

maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
