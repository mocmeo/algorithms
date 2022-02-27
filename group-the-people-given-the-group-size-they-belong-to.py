def groupThePeople(groupSizes):
	mapper = {}
	res = []
	for i in range(len(groupSizes)):
		size = groupSizes[i]
		if size in mapper:
			mapper[size].append(i)
		else:
			mapper[size] = [i]

	for size in mapper:
		i = 0
		while i < len(mapper[size]):
			res.append(mapper[size][i:i+size])
			i += size

	return res

print(groupThePeople([3,3,3,3,3,1,3]))
print(groupThePeople([2,1,3,3,3,2]))