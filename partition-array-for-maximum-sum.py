def maxSumAfterPartitioning(arr, k):
	F = [0]*len(arr)
	for i in range(len(arr)):
		max_sub = 0
		for j in range(1,k+1):
			if i-j+1 >= 0:
				max_sub = max(max_sub, arr[i-j+1])
				if i - j < 0:
					F[i] = max(F[i], max_sub*j)
				else:
					F[i] = max(F[i], F[i-j] + max_sub*j)
	return F[-1]

print(maxSumAfterPartitioning([1,15,7,9,2,5,10], 3))
print(maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4))
print(maxSumAfterPartitioning([1], 1))
print(maxSumAfterPartitioning([3,7], 2))

	