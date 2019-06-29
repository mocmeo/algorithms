def hammingWeight(n):
    result = 0
    for ch in str(n):
        if ch == '1':
            result += 1
    return result


print(hammingWeight("00000000000000000000000000001011"))
