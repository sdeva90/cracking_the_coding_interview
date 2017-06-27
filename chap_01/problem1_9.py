def str_rotate(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 * 2


if __name__ == "__main__":
    print(str_rotate("waterbottle", "erbottlewat"))
