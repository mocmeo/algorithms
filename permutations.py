def permute(nums):
	arr = []
	res = []
	visited = set({})

	def generate(arr, visited, nums):
		if len(arr) == len(nums):
			res.append(arr[:])
			return
		for num in nums:
			if num not in visited:
				arr.append(num)
				visited.add(num)
				generate(arr, visited, nums)
				arr.pop()
				visited.remove(num)

	generate(arr, visited, nums)
	return res

print(permute([1,2,3]))
# print(permute([0,1]))