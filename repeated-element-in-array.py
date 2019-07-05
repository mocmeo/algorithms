from collections import Counter


def repeatedNTimes(A):
    freq = Counter(A)
    n = int(len(A) / 2)
    result = list(filter(lambda x: freq[x] == n, A))
    return result[0]


print(repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
