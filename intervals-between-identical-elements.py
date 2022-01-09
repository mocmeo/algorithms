def getDistances(arr):
	mapper = {}
	F = [0]*len(arr)

	for i in range(len(arr)):
		num = arr[i]
		if num in mapper:
			F[i] += i*mapper[num][0] - mapper[num][1]
			mapper[num][0] += 1
			mapper[num][1] += i
		else:
			F[i] = 0
			mapper[num] = [1, i]

	mapper = {}
	for i in range(len(arr)-1,-1,-1):
		num = arr[i]
		if num in mapper:
			F[i] += mapper[num][1] - i*mapper[num][0]
			mapper[num][0] += 1
			mapper[num][1] += i
		else:
			mapper[num] = [1, i]
	
	return F


print(getDistances([2,1,3,1,2,3,3]))
print(getDistances([10,5,10,10]))