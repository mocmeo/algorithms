def maximumProduct(nums):
    nums.sort()
    result = max(nums[-1]*nums[-2]*nums[-3],
                 nums[0]*nums[1]*nums[2],
                 nums[0]*nums[1]*nums[-1],
                 nums[0]*nums[-2]*nums[-1])
    return result


print(maximumProduct([1, 2, 3, 4]))
