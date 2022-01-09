def peek(seq):
	return seq[len(seq)-1]

def canSeePersonsCount(heights):
	seq = []
	res = []
	for i in range(len(heights)-1, -1, -1):
		count = 0
		while len(seq) > 0 and peek(seq) < heights[i]:
			seq.pop()
			count += 1
		if len(seq) > 0:
			count += 1

		seq.append(heights[i])
		res.append(count)
	
	return res[::-1]
		

# print(canSeePersonsCount([10,6,8,5,11,9]))
# print(canSeePersonsCount([3,2,0,1,4]))
print(canSeePersonsCount([0,1,0,2,1,0,1,3,2,1,2,1]))
