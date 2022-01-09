def firstMissingPositive(nums):
	mapper = {item:idx for idx, item in enumerate(nums)}
	seen = {}
	res = max(nums)+1

	if 1 not in mapper:
		return 1

	for k, v in mapper.items():
		print(k)
		if k in seen:
			continue
		else:
			seen[k] = 1
			l = k
			r = k
			while l in mapper:
				seen[l] = 1
				l -= 1
			while r in mapper:
				seen[r] = 1
				r += 1
			if l > 0 and l < res:
				res = l
			if r > 0 and r < res:
				res = r
	return res

print(firstMissingPositive([7,8,9,11,12]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([1,1000]))