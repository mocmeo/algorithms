def getMinSwaps(num, k):
	arr = []
	res = 0
	for ch in num:
		arr.append(ch - '0')

	for i in range(len(arr)-1, -1, 0):
		if arr[i-1] < arr[i]:


	