def isPalindrome(x):
    strNum = str(x)

    for i in range(0, int(len(strNum) / 2)):
        if (strNum[i] != strNum[len(strNum) - i - 1]):
            return False
    return True


print(isPalindrome(-121))
