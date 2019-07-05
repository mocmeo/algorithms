def findNthDigit(n):
    count = 0
    k = 0
    power = 1
    p = 10
    while count < n:
        k += 1
        if k >= p:
            power += 1
            p *= 10
        count += power

    if count == n:
        return k % 10
    else:  # count > n
        temp = count - n
        digit = str(k)[len(str(k)) - temp - 1]
        return int(digit)


print(findNthDigit(1000000000))
