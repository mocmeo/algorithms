def checkLastPosition(pos, startDict, endDict):
    for ch in startDict.keys():
        if startDict[ch] <= pos and endDict[ch] > pos:
            return False
    return True


def partitionLabels(S):
    startDict, endDict = {}, {}

    for i, ch in enumerate(S):
        if startDict.get(ch) is None:
            startDict[ch] = i
        endDict[ch] = i

    x = 0
    result = []
    startPos = 0
    while x < len(S):
        lastPos = endDict[S[x]]
        if checkLastPosition(lastPos, startDict, endDict):
            # result.append(S[startPos:lastPos+1])
            result.append(len(S[startPos:lastPos+1]))
            x = lastPos + 1
            startPos = lastPos + 1
        else:
            x += 1
    return result


print(partitionLabels(""))
