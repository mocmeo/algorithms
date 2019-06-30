def duplicateZeros(arr):
    i = 0
    while i < len(arr):
        if (arr[i] == 0):
            arr.insert(i, 0)
            del arr[-1]
            i += 1
        i += 1
    return arr


print(duplicateZeros([1, 2, 3]))
