def findMaxAverage(nums, k):
    F = []
    sumF = 0
    for i in range(len(nums)):
        sumF += nums[i]
        F.append(sumF)

    result = float(F[k-1])
    current_sum = float(F[k-1])
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        result = max(result, current_sum)
    return result / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
