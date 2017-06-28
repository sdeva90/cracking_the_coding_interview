# 1.6 string compression
s1 = "gkdkkssjjffddggg"
ans = ""
count = 1
for i in range(len(s1)):
    if i == len(s1) - 1 or s1[i] != s1[i+1]:
        ans += s1[i] + str(count)
        count = 0
    count = count + 1
print(ans if len(ans) >= len(s1) else s1)
