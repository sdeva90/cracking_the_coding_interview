# 1.4 palindrom - permutation
t = {}
s = "tattaasta"
for x in s:
    t[x] = t.get(x, 0)^1
if sum(t.values()) < 2:
    print("true")
else:
    print("f")
