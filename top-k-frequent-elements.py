# def topKFrequent(nums, k):
# 	count = {}
# 	rev_count = {}
# 	res = []
# 	for num in nums:
# 		if num in count:
# 			count[num] += 1
# 		else:
# 			count[num] = 1
	
# 	for num in count.keys():
# 		freq = count[num]
# 		if freq in rev_count:
# 			rev_count[freq].append(num)
# 		else:
# 			rev_count[freq] = [num]

# 	for freq in range(len(nums), -1, -1):
# 		if freq in rev_count:
# 			qty = len(rev_count[freq])
# 			if k >= qty:
# 				k -= qty
# 				res.extend(rev_count[freq])
# 			else:
# 				res.extend(rev_count[freq][:k])
# 				break
# 	return res

# print(topKFrequent([1,1,1,2,2,3,3,3],2))
# print(topKFrequent([1],1))

import heapq
from collections import Counter

def topKFrequent(nums, k):
	count = Counter(nums)
	heap = []
	res = []

	for key in count:
		heapq.heappush(heap, [count[key], key])
		if len(heap) > k:
			heapq.heappop(heap)

	return [x[1] for x in heap]

print(topKFrequent([1,1,1,2,2,3], 2))