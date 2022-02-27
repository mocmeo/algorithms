def getPower(x):
	power = 0
	while x != 1:
		if x&1:
			x = 3*x + 1
		else:
			x //= 2
		power += 1
	return power

def getKth(lo, hi, k):
	arr = []
	for i in range(lo, hi+1):
		arr.append([getPower(i), i])

	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			if arr[i][0] > arr[j][0]:
				arr[i], arr[j] = arr[j], arr[i]
			if arr[i][0] == arr[j][0] and arr[i][1] > arr[j][1]:
				arr[i], arr[j] = arr[j], arr[i]

	return arr[k-1][1]

print(getKth(12, 15, 2))
print(getKth(7, 11, 4))
