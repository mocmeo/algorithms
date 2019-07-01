def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = j = 0
    result = []
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i] < nums2[j]:
                while i < len(nums1) and nums1[i] < nums2[j]:
                    i += 1
            else:
                while j < len(nums2) and nums2[j] < nums1[i]:
                    j += 1
    return list(set(result))


def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = j = 0
    result = []
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        else:
            if nums1[i] < nums2[j]:
                while i < len(nums1) and nums1[i] < nums2[j]:
                    i += 1
            else:
                while j < len(nums2) and nums2[j] < nums1[i]:
                    j += 1
    return result


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
