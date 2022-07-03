def subsetsWithDup(nums):
	nums = sorted(nums)
	arr = [[]]
	myset = set({})
	for num in nums:
		temp = []
		for cur in arr:
			x = cur + [num]
			xstr = "".join(str(n) for n in x)
			if xstr not in myset:
				myset.add(xstr)
				temp.append(x)
		arr += temp
	return arr

print(subsetsWithDup([4,4,4,1,4]))
