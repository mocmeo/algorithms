def lemonadeChange(bills):
    numFive = numTen = 0
    for x in bills:
        if x == 5:
            numFive += 1
        elif x == 10:
            if numFive == 0:
                return False
            else:
                numFive -= 1
                numTen += 1
        elif x == 20:
            if numTen > 0:
                if numFive == 0:
                    return False
                else:
                    numFive -= 1
                    numTen -= 1
            else:
                if numFive < 3:
                    return False
                else:
                    numFive -= 3
    return True


print(lemonadeChange([]))
