from collections import Counter

def checkIfExist(arr):
	count = Counter(arr)

	for _, num in enumerate(count):
		if num == 0 and count[num] == 2:
			return True
		if num * 2 in count and num != num * 2:
			return True

	return False

# print(checkIfExist([10,2,5,3]))
# print(checkIfExist([7,1,14,11]))
# print(checkIfExist([3,1,7,11]))
print(checkIfExist([-2,0,10,-19,4,6,-8]))
print(checkIfExist([0, 0]))
