def numSubseq(nums, target):
	nums.sort()
	mod = 10**9 + 7
	F = [1]
	right = len(nums)-1
	left = 0
	res = 0
	for i in range(1, len(nums)+1):
			F.append((F[i-1] * 2) % mod)

	while left <= right:
			if nums[left] + nums[right] <= target:
					res = (res + F[right-left]) % mod
					left += 1
			else:
					right -= 1

	return res

print(numSubseq([2,3,3,4,6,7], 12))
print(numSubseq([3,3,6,8], 10))
print(numSubseq([3,5,6,7], 9))
print(numSubseq([5,2,4,1,7,6,8], 16))
print(numSubseq([1], 1))
print(numSubseq([1,2,3,4], 12))



	