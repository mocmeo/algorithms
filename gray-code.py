def grayCode(n):
	arr = [0,1,3,2]
	x = 2
	while x < n:
		new_arr = []
		for i in range(len(arr)-1, -1, -1):
			new_arr.append((1 << x) ^ arr[i])
		
		arr.extend(new_arr)
		x += 1
	return arr[:1<<n]
	

print(grayCode(16))