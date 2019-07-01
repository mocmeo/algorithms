def moveZeroes(nums):
    i = 0
    j = len(nums)-1

    while i < j:
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
        else:
            i += 1
        if nums[j] == 0:
            j -= 1
    return nums


print(moveZeroes([0, 0, 1]))
