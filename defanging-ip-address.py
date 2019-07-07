def defangIPaddr(address):
    result = ""
    for ch in address:
        if ch != '.':
            result += ch
        else:
            result += '[.]'
    return result


print(defangIPaddr("1.1.1.1"))
