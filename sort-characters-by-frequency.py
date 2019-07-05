from collections import Counter


def frequencySort(s):
    F = [[] for i in range(len(s)+1)]
    count = Counter(s)

    for ch in count.keys():
        freq = count[ch]
        F[freq].append(ch)

    answer = ""
    for x in range(len(s), -1, -1):
        if len(F[x]) > 0:
            for ch in F[x]:
                answer += ch*x
    return answer


print(frequencySort("a"))
