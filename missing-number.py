def missingNumber(nums):
    arr = [False for x in range(0, len(nums)+1)]
    for x in nums:
        arr[x] = True
    for i in range(0, len(arr)):
        if not arr[i]:
            return i


print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
