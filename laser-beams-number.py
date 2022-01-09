def numberOfBeams(bank):
	arr = []
	for i in range(len(bank)):
		row_sum = 0
		for j in range(len(bank[i])):
			row_sum += 1 if bank[i][j] == "1" else 0
		arr.append(row_sum)

	res = 0
	pt = 0
	for i in range(len(arr)):
		if arr[i] == 0:
			continue
		if arr[i] > 0 and pt > 0:
			res += arr[i]*pt
			pt = arr[i]
		else:
			pt = arr[i]

	return res
	
        
print(numberOfBeams(["011001","000000","010100","001000"]))
print(numberOfBeams(["000","111","000"]))