def binaryGap(N):
    result, count = 0, 0
    found = False
    while N > 0:
        mod = N % 2
        if found:
            count += 1
            if mod == 1:
                result = max(result, count)
                count = 0
        else:
            if mod == 1:
                found = True
        N = int(N/2)
    return result


print(binaryGap(9))
