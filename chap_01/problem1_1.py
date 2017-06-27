def isUnique(s):
    table = {}
    for ch in s:
        if ch in table:
            return False
        table[ch] = 1
    return True


def isUnique_2(s):
    s = sorted(list(s))
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return False
    return True


def isUnique_3(s):
    num = 0
    for i in range(len(s)):
        pos = (1 << (ord(s[i]) - ord('a')))
        if pos & num:
            return False
        num |= pos
    return True

if __name__ == "__main__":
    print(isUnique_3("abcde"))
    print(isUnique_3("abacd"))
