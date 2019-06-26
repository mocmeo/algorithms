def lengthOfLastWord(s):
    strs = s.strip().split(' ')
    return len(strs[-1])


print(lengthOfLastWord("a "))
