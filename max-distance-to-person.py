def maxDistToClosest(seats):
    # indices of occupied seats
    seatIndex = []
    for i in range(len(seats)):
        if (seats[i] == 1):
            seatIndex.append(i)

    result = max(seatIndex[0], len(seats) - seatIndex[-1] - 1)
    if (len(seatIndex) == 1):
        return result

    for i in range(0, len(seatIndex)):
        if (seatIndex[i] - seatIndex[i-1] > 1):
            avgDist = int((seatIndex[i] - seatIndex[i-1])/2)
            result = max(result, avgDist)
    return result


print(maxDistToClosest([0, 0, 1, 0, 1, 1]))
