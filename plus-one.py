def toNumber(digits):
    result = 0
    for digit in digits:
        result = result*10 + digit
    return result


def toDigits(num):
    result = []
    while (num > 0):
        result.insert(0, num % 10)
        num = int(num / 10)
    return result


def plusOne(digits):
    num = toNumber(digits)
    num += 1
    return toDigits(num)


print(plusOne([0]))
