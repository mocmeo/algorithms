def combinationSum(candidates, target):
	path = []
	res = []

	def generate(candidates, target, idx):
		if sum(path) == target:
			res.append(path[:])
		if sum(path) > target:
			return
		for i in range(idx, len(candidates)):
			path.append(candidates[i])
			generate(candidates, target, i)
			path.pop()

	generate(candidates, target, 0)
	return res

# print(combinationSum([2,3,5], 8))
# print(combinationSum([2,3,5], 300))
