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


print(shortestToChar("e", "e"))
