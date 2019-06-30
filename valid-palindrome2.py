def isPalindrome(s):
    return s == s[::-1]


def validPalindrome(s):
    left = 0
    right = len(s) - 1
    while (left <= right):
        if (s[left] == s[right]):
            left += 1
            right -= 1
        else:
            return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
    return True


print(validPalindrome("aba"))
