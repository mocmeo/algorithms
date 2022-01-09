def dfs(idx, arr, F):
	if F[idx]:
		return
	
	F[idx] = 1
	if idx + arr[idx] < len(arr):
		dfs(idx + arr[idx], arr, F)
	if idx - arr[idx] >= 0:
		dfs(idx - arr[idx], arr, F)

def canReach(arr, start):
	F = [0]*len(arr)
	res = [0]*len(arr)
	dfs(start, arr, F)

	for i in range(len(F)):
		if arr[i] == 0 and F[i]:
			return True 

	return False

print(canReach([4,2,3,0,3,1,2], 5))
print(canReach([4,2,3,0,3,1,2], 0))
print(canReach([3,0,2,1,2], 2))
