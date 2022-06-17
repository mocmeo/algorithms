from curses import curs_set


def combinationSum2(candidates, target):
	path = []
	res = []
	candidates.sort()

	def generate(candidates, target, idx):
		sump = sum(path)
		if sump == target:
			res.append(path[:])

		if sump > target:
			return
		
		for i in range(idx, len(candidates)):
			if i > idx and candidates[i] == candidates[i-1]:
				continue
			path.append(candidates[i])
			generate(candidates, target, i+1)
			path.pop()
	generate(candidates, target, 0)
	
	return res

print(combinationSum2([10,1,2,7,6,1,5], 8))
print(combinationSum2([2,5,2,1,2], 5))
print(combinationSum2([3,3,3,4], 9))