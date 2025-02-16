n = int(input())
j = m = h = 0
for _ in range(n):
    s = input().replace(" ", "")
    j += s[0] == "J"
    m += s[1] == "J"
    h += s[2] == "J"
res = min(j, m, h)
print(res)
