import heapq

def medianSlidingWindow(nums, k):
	small, large = [], []
	if k % 2 == 0:
		small_cnt, large_cnt = k/2, k/2
	else:
		small_cnt, large_cnt = k//2+1, k//2

	res = []
	large_cnt = 2
	for i in range(len(nums)):
		heapq.heappush(small, -nums[i])
		heapq.heappush(large, nums[i])
		if len(large) > large_cnt:
			heapq.heappop(large)
		if len(small) > small_cnt:
			heapq.heappop(small)

		print(large[0])
		# if i >= k-1:
		# 	if k % 2 == 0:
		# 		new_num = (-small[0] + large[0])*0.5
		# 	else:
		# 		new_num = -small[0]
		# 	res.append(new_num)
	return res

	
print(medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))