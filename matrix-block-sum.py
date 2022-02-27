def calc(F, i, j, k):
	m, n = len(F), len(F[0])
	x1, y1 = i+k, j+k
	x, y = i-k-1, j-k-1

	if x1 >= m:
		x1 = m-1
	if y1 >= n:
		y1 = n-1
	
	top = F[x][y1] if x >= 0 else 0
	left = F[x1][y] if y >= 0 else 0
	topleft = F[x][y] if x >= 0 and y >= 0 else 0

	return F[x1][y1] - top - left + topleft


def matrixBlockSum(mat, k):
	m, n = len(mat), len(mat[0])
	F = [[0]*n for i in range(m)]
	res = [[0]*n for i in range(m)]

	for i in range(m):
		for j in range(n):
			x, y = i-1, j-1
			
			top = F[x][j] if x >= 0 else 0
			left = F[i][y] if y >= 0 else 0
			topleft = F[x][y] if x >= 0 and y >= 0 else 0
			F[i][j] = top + left - topleft + mat[i][j]

	for i in range(m):
		for j in range(n):
			res[i][j] = calc(F, i, j, k)
	return res

print(matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
print(matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
