def projectionArea(grid):
	res = 0
	for i in range(len(grid)):
		max_row = 0
		for j in range(len(grid[0])):
			if grid[i][j] > 0:
				res += 1
				max_row = max(max_row, grid[i][j])
		res += max_row

	for j in range(len(grid[0])):
		max_col = 0
		for i in range(len(grid)):
			max_col = max(max_col, grid[i][j])
		res += max_col

	return res

print(projectionArea([[1,2],[3,4]]))
print(projectionArea([[2]]))
print(projectionArea([[1,0],[0,2]]))
	