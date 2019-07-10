from collections import Counter


def leastInterval(tasks, n):
    if n == 0:
        return len(tasks)
    freq = Counter(tasks)
    maxFreq = max(freq.values())
    countMaxFreq = 0
    for task in freq.keys():
        if freq[task] == maxFreq:
            countMaxFreq += 1

    if len(tasks) / maxFreq > n:
        return len(tasks)
    else:
        # return (maxFreq*(n+1)) - (n + 1 - max(countMaxFreq, len(tasks) - (n+1)*(maxFreq - 1)))
        return maxFreq*(n+1) - (n + 1 - countMaxFreq)


# print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))
# print(leastInterval(["A", "B"], 1))
print(leastInterval(["A", "A", "A", "B", "B", "C", "C", "D"], 2))
