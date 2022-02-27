from tkinter import N

def minMoves(nums, limit):
	mapper = {}
	n = len(nums)
	for i in range(n//2):
		cur_sum = nums[i] + nums[n-i-1]
		mapper[cur_sum] = mapper

# print(minMoves([1,2,4,3], 4))
# print(minMoves([1,2,2,1], 2))
# print(minMoves([1,2,1,2], 2))
print(minMoves([28,50,76,80,64,30,32,84,53,8], 84))
	


