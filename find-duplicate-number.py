def findDuplicate(nums):
    for i in range(len(nums)):
        cur = abs(nums[i])
        if nums[cur] < 0:
            return abs(nums[i])
        else:
            nums[cur] *= -1

print(findDuplicate([1,2,2]))

  
