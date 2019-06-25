def twoSum(nums, target: int):
    length = len(nums)
    for x in range(0, length):
        num_x = nums[x]
        num_y = target - num_x
        if num_y in nums:
            y = nums.index(num_y)
            if x != y:
                return [x, y]


print(twoSum([2, 7, 11, 15], 9))
