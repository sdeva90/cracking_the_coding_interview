s1 = "carrot"
s2 = "cotarr"
a = sorted(s1)
b = sorted(s2)
if a==b:
    print("done")
table = {}
s1 = "carrot"
s2 = "cotarr"
for a in s1:
    table[a] = table.get(a, 0)+ 1
for a in s2:
    if a not in table:
        print("not permutation")
        break
    table[a] -= 1
if all(table[elem] == 0 for elem in table):
    print("good")
