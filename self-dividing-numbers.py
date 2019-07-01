def isValid(num):
    for ch in str(num):
        if ch == '0':
            return False
        if num % int(ch) != 0:
            return False
    return True


def selfDividingNumbers(left, right):
    result = []
    for x in range(left, right+1):
        if isValid(x):
            result.append(x)
    return result


print(selfDividingNumbers(1, 22))
