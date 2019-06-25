def toNumber(binary):
    result = 0
    for (i, digit) in enumerate(reversed(binary)):
        result += int(digit) * (2**i)
    return result


def toBinary(num):
    if (num == 0):
        return "0"

    result = ""
    while (num > 0):
        result = str(num % 2) + result
        num = int(num / 2)
    return result


def addBinary(a, b):
    result = toNumber(a) + toNumber(b)
    return toBinary(result)


print(addBinary("0", "0"))
