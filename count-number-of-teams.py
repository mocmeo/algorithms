def numTeams(rating):
	A = []
	D = []
	res = 0
	for i in range(len(rating)):
		asc = 0
		desc = 0
		for j in range(i+1, len(rating)):
			if rating[j] > rating[i]:
				asc += 1
			else:
				desc += 1
		A.append(asc)
		D.append(desc)

	for i in range(len(rating)-2):
		for j in range(i+1, len(rating)-1):
			if rating[j] > rating[i]:
				res += A[j]
			else:
				res += D[j]
	return res

print(numTeams([2,5,3,4,1]))
print(numTeams([2,1,3]))
print(numTeams([1,2,3,4]))
