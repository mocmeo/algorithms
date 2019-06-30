def numJewelsInStones(J, S):
    result = 0
    for ch in J:
        result += S.count(ch)
    return result


print(numJewelsInStones("z", "ZZ"))
