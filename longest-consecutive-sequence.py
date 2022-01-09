def longestConsecutive(nums):
	numSet = set(nums)
	seen = {}
	res = 0
	for k in numSet:
		if k in seen:
			continue
		else:
			seen[k] = 1
			l = k
			r = k
			while l in numSet:
				seen[l] = 1
				l -= 1
			while r in numSet:
				seen[r] = 1
				r += 1
			res = max(res, r-l-1)

	return res

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([-8,-4,9,9,4,6,1,-4,-1,6,8]))
  