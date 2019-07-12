def findMaxConsecutiveOnes(nums):
    if not nums:
        return 0

    nums.append(0)
    nums.insert(0, 0)
    prev = 0
    result = 0
    for i in range(1, len(nums)):
        if nums[i] == 0 and nums[i-1] == 1:
            result = max(result, i - prev)
        if nums[i] == 1 and nums[i-1] == 0:
            prev = i
    return result


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
