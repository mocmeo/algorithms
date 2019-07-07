def productExceptSelf(nums):
    n = len(nums)
    leftArr = [0]*n
    rightArr = [0]*n

    leftArr[0], leftArr[1] = 1, nums[0]
    rightArr[-1], rightArr[-2] = 1, nums[-1]

    for i in range(2, n):
        leftArr[i] = leftArr[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        rightArr[i] = rightArr[i+1] * nums[i+1]

    result = []
    for i in range(n):
        if i == 0:
            result.append(rightArr[i])
        elif i == n-1:
            result.append(leftArr[i])
        else:
            result.append(leftArr[i]*rightArr[i])
    return result


print(productExceptSelf([1, 2, 0, 4]))
