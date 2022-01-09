def cache(grid):
	F = [[0]*len(grid[0]) for i in range(len(grid))]
	F[0][0] = grid[0][0]

	for j in range(1, len(grid[0])):
		F[0][j] = F[0][j-1] + grid[0][j]
	
	for i in range(1, len(grid)):
		F[i][0] = F[i-1][0] + grid[i][0]

	for i in range(1, len(grid)):
		for j in range(1, len(grid[0])):
			F[i][j] = F[i-1][j] + F[i][j-1] - F[i-1][j-1] + grid[i][j]
	return F

def calc(F, x, y, x1, y1):
	if x < 0: 
		x = 0
	if y < 0:
		y = 0
	if x == 0 and y == 0:
		return F[x1][y1]
	if x > 0 and y > 0:
		return F[x1][y1] - F[x-1][y1] - F[x1][y-1] + F[x-1][y-1]
	elif x == 0:
		return F[x1][y1] - F[x1][y-1]
	else:
		return F[x1][y1] - F[x-1][y1]

def possibleToStamp(grid, stampHeight, stampWidth):
	F = cache(grid)
	grid2 = [[0]*len(grid[0]) for i in range(len(grid))]

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			x, y = i + stampHeight - 1, j + stampWidth - 1

			if x < len(grid) and y < len(grid[0]):
				if calc(F, i, j, x, y) == 0 and grid[i][j] != 1:
					grid2[i][j] = 1

	
	F2 = cache(grid2)
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				if calc(F2, i-stampHeight+1, j-stampWidth+1, i, j) == 0:
					return False
	
	return True

print(possibleToStamp([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 4, 3))
print(possibleToStamp([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 2))