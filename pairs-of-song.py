from collections import Counter


def numPairsDivisibleBy60(time):
    numDict = Counter()
    for t in time:
        numDict[t % 60] += 1

    result = int(numDict[0]*(numDict[0]-1)/2) if numDict[0] else 0
    result += int(numDict[30]*(numDict[30]-1)/2) if numDict[30] else 0
    for x in range(31, 60):
        y = 60-x
        result += numDict[x]*numDict[y]
    return result


print(numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(numPairsDivisibleBy60([60, 60, 60]))
