from collections import Counter

def findFinalValue(nums, original):
	count = Counter(nums)

	while original in count:
		original *= 2
	return original

print(findFinalValue([5,3,6,1,12], 3))
print(findFinalValue([2,7,9], 4))
