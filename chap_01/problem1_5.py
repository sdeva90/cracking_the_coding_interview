def oneway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif edited:
            return False
        else:
            edited = True
            if len(s1) == len(s2):  # Replace
                i += 1
                j += 1
            else:   # Insert / Remove
                j += 1
    return True


if __name__ == "__main__":
    print(oneway("pale", "pal"))
    print(oneway("pales", "pale"))
    print(oneway("pale", "bale"))
    print(oneway("pale", "bae"))
