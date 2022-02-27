def findLengthOfShortestSubarray(arr):
	stack = []
	res = 0
	for i in range(len(arr)):
		while stack and stack[-1] > arr[i]:
			stack.pop()
			res += 1
		stack.append(arr[i])

	return res

print(findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
# print(findLengthOfShortestSubarray([5,4,3,2,1]))
# print(findLengthOfShortestSubarray([1,2,3]))
# print(findLengthOfShortestSubarray([2,2,2,1,1,1]))
print(findLengthOfShortestSubarray([11,26,3,14,24,6,10,16,32,9,36,24,27,17,31,32,35,36,11,22,30]))
		
		