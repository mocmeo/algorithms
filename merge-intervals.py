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
            del intervals[x+1]
            intervals[x] = common
        else:
            x += 1
    return intervals


def merge2(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            maxEnd = max(merged[-1][1], interval[1])
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


# print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge2([[1, 4], [4, 5]]))
print(merge2([[4, 5], [7, 8]]))
print(merge2([[1, 4], [5, 6]]))
