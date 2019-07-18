def findErrorNums(nums):
    arr = [0]*(len(nums) + 1)
    for num in nums:
        arr[num] += 1

    result = []
    for i in range(len(arr)):
        if i > 0:
            if arr[i] > 1:
                result.insert(0, i)
            if arr[i] == 0:
                result.append(i)
    return result


print(findErrorNums([1, 1]))
