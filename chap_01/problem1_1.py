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

if __name__ == "__main__":
    print(isUnique_2("abcde"))
    print(isUnique_2("abacd"))
