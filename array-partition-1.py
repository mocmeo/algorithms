def arrayPairSum(nums):
    nums.sort()
    n = int(len(nums)/2)
    result = 0
    for i in range(n):
        result += nums[i*2]
    return result


print(arrayPairSum([1, 1]))
