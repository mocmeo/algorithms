def isCovered(ranges, left, right):
	mapper = {}
	for vals in ranges:
		for i in range(vals[0], vals[1]+1):
			mapper[i] = 1
	
	for i in range(left, right+1):
		if i not in mapper:
			return False
	return True

print(isCovered([[1,2],[3,4],[5,6]], 2, 5))
print(isCovered([[1,10],[10,20]], 21, 21))