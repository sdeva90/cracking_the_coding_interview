def urlify(string, length):
    string = list(string)
    index = len(string)
    for i in range(length - 1, -1, -1):
        if string[i] == ' ':
            string[index - 3: index] = '%20'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    return "".join(string)

if __name__ == "__main__":
    print(urlify("Mr John Smith    ", 13))
