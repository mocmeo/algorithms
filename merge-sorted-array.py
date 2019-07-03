import sys


def merge(nums1, m, nums2, n):
    x, y = 0, 0
    for i in range(0, len(nums1)):
        if i >= m:
            nums1[i] = sys.maxsize

    while x < m+n and y < n:
        while x < m+n and nums1[x] < nums2[y]:
            x += 1
        nums1.insert(x, nums2[y])
        nums1.pop()
        y += 1

    k = len(nums1) - 1
    while nums1[k] == sys.maxsize:
        nums1.pop()
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1], 1, [], 0))
print(merge([1, 0], 1, [2], 1))
print(merge([2, 0], 1, [1], 1))
print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
print(merge(
    [-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
