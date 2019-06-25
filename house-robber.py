def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    arr = [0 for x in range(0, len(nums)+1)]
    arr[0] = nums[0]
    arr[1] = max(arr[0], nums[1])
    for x in range(2, len(nums)):
        arr[x] = max(arr[x-2] + nums[x], arr[x-1])
    return arr[len(nums) - 1]


print(rob([2, 7, 9, 3, 1]))
