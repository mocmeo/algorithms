def heightChecker(heights):
    sortedArr = sorted(heights)
    count = 0
    for a, b in zip(sortedArr, heights):
        if a != b:
            count += 1
    return count


print(heightChecker([1, 1, 4, 2, 1, 3]))
