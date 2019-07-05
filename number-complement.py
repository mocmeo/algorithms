def findComplement(num):
    bit = 1
    while bit <= num:
        bit <<= 1
    bit -= 1
    return num ^ bit


print(findComplement(1))
