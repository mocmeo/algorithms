def maximumEvenSplit(finalSum):
	if finalSum % 2 != 0:
		return []

	sumd = 0
	x = 0
	mapper = {}
	while sumd < finalSum:
		x += 2
		sumd += x
		mapper[x] = 1
		if sumd == finalSum:
			return mapper.keys()
	
	sumd -= x
	mapper[x] = 0
	temp_x = x
	x = finalSum - sumd

	mapper[temp_x - 2] = 0
	mapper[temp_x + x - 2] = 1

	res = []
	for key in mapper.keys():
		if mapper[key] > 0:
			res.append(key)
	return res

# print(maximumEvenSplit(12))
# print(maximumEvenSplit(28))
# print(maximumEvenSplit(7))
# print(maximumEvenSplit(46))
# print(maximumEvenSplit(50))
print(maximumEvenSplit(8))
print(maximumEvenSplit(46))
