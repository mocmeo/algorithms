from collections import Counter


def findAnagrams(s, p):
    if len(s) < len(p):
        return []

    strDict = Counter(s[0:len(p)])
    pDict = Counter(p)
    answer = []

    if (strDict == pDict):
        answer.append(0)

    for i in range(1, len(s) - len(p) + 1):
        left = s[i-1]
        right = s[i+len(p)-1]

        strDict[left] -= 1
        strDict[right] += 1
        if strDict[left] == 0:
            del strDict[left]

        if (strDict == pDict):
            answer.append(i)
    return answer


print(findAnagrams("cbaebabacd", "abc"))
