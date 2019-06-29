def isPalindrome(s):
    strArr = ""
    for ch in s:
        if (ch.isalnum()):
            strArr += ch.lower()
    return strArr == strArr[::-1]


print(isPalindrome(""))
