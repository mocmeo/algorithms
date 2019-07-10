def reachNumber(target):
    target = abs(target)
    count = sumX = 0
    while sumX < target:
        count += 1
        sumX += count

    if sumX == target:
        return count
    else:
        diff = sumX - target
        if diff % 2 == 0:
            return count
        else:
            return count+1


print(reachNumber(22))
