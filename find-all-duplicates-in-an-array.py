from collections import Counter

def findDuplicates(nums):
	count = Counter(nums)
	res = []

	for num in count:
		if count[num] == 2:
			res.append(num)

	return res

print(findDuplicates([4,3,2,7,8,2,3,1]))
print(findDuplicates([1,1,2]))
print(findDuplicates([1]))

