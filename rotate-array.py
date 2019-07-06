def rotate(nums, k):
    if nums:
        k = k % len(nums)
        if k == 0:
            return nums
    n = len(nums)
    nums[:] = nums[-k:] + nums[0:n-k]
    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 4))
