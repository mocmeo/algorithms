def exist(board, word):
	width = len(board[0])
	height = len(board)

	def dfs(x, y, i, visited):
		# print(x, y, board[x][y], i)
		
		calc = x*width + y
		flag = False
		if calc in visited:
			if i < visited[calc]:
				return False
		else:
			visited[calc] = i

		if board[x][y] != word[i]:
			return False
		if i == len(word) - 1 and board[x][y] == word[i]:
			return True
		if i >= len(word):
			return False
		
		if i < len(word)-1:
			if x-1 >= 0: 
				if board[x-1][y] == word[i+1]: 
					flag = dfs(x-1, y, i+1, visited)
					if flag: return flag
			if y-1 >= 0: 
				if board[x][y-1] == word[i+1]: 
					flag = dfs(x, y-1, i+1, visited)
					if flag: return flag
			if x+1 <= height-1: 
				if board[x+1][y] == word[i+1]: 
					flag = dfs(x+1, y, i+1, visited)
					if flag: return flag
			if y+1 <= width-1: 
				if board[x][y+1] == word[i+1]: 
					flag = dfs(x, y+1, i+1, visited)
					if flag: return flag
		else:
			if board[x][y] == word[i]:
				return True
		return flag

	for i in range(height):
		for j in range(width):
			if dfs(i, j, 0, {}):	
				return True
	return False

# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
# print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
