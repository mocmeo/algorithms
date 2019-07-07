def checkMatch(first, second):
    if first[1] >= second[0] and first[0] <= second[1]:
        return [min(first[0], second[0]), max(first[1], second[1])]
    return []


def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort()
    x = 0
    while x < len(intervals) - 1:
        common = checkMatch(intervals[x], intervals[x+1])
        if common:
            del intervals[x]
            del intervals[x]
            intervals.insert(x, common)
        else:
            x += 1
    return intervals


# print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
print(merge([[4, 5], [7, 8]]))
print(merge([[1, 4], [5, 6]]))
