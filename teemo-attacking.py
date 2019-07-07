def findPoisonedDuration(timeSeries, duration):
    result = 0
    for i in range(len(timeSeries)):
        if i < len(timeSeries) - 1:
            finishedTime = timeSeries[i] + duration
            if finishedTime < timeSeries[i+1]:
                result += duration
            else:
                result += timeSeries[i+1] - timeSeries[i]
        else:
            result += duration
    return result


print(findPoisonedDuration([1, 2], 2))
