def corpFlightBookings(bookings, n):
    F = [[0, 0] for i in range(n+1)]
    for item in bookings:
        i, j, val = item[0], item[1], item[2]
        F[i][0] += val
        F[j][1] += val

    result = []
    count = 0
    for i in range(1, n+1):
        count += F[i][0]
        result.append(count)
        count -= F[i][1]
    return result


print(corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
