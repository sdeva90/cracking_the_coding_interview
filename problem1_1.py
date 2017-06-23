def isUnique(s):
    table = {}
    for ch in s:
        if ch in table:
            return False
        table[ch] = 1
    return True
