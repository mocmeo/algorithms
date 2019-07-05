def shortestToChar(S, C):
    charIndex = []
    for i in range(len(S)):
        if (S[i] == C):
            charIndex.append(i)

    result = []
    for i in range(len(S)):
        dist = len(S)
        for index in charIndex:
            dist = min(dist, abs(i - index))
        result.append(dist)
    return result


def shortestToChar2(S, C):
    prev = float('-inf')
    result = []
    for i, x in enumerate(S):
        if x == C:
            prev = i
        result.append(i - prev)

    for i in range(len(S) - 1, -1, -1):
        if S[i] == C:
            prev = i
        result[i] = min(result[i], prev - i)
    return result


print(shortestToChar2("loveleetcode", "e"))
