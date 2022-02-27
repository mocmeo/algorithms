from collections import Counter
def maxOperations(nums, k):
	count = Counter(nums)
	res = 0
	for v in count.keys():
		min_cnt = min(count.get(v, 0), count.get(k-v, 0))
		res += min_cnt
	return res // 2

print(maxOperations([3,1,3,4,3], 6))
print(maxOperations([1,2,3,4], 5))
