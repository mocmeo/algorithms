def maxProduct(nums):
    if not nums:
        return 0
    minBand = [0]*len(nums)
    maxBand = [0]*len(nums)
    minBand[0] = maxBand[0] = nums[0]

    result = nums[0]
    for i in range(1, len(nums)):
        n1 = minBand[i-1]*nums[i]
        n2 = maxBand[i-1]*nums[i]
        maxBand[i] = max(max(n1, n2), nums[i])
        minBand[i] = min(min(n1, n2), nums[i])
        result = max(result, maxBand[i])
    return result


print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
