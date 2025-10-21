n = int(input())
s, cnt = [0] * 5, [0] * 5
for _ in range(n):
    c, p = (int(i) for i in input().split())
    s[c - 1] += p
    cnt[c - 1] += 1
res = 0
for i in range(5):
    s[i] //= cnt[i]
    if s[i] < s[res]:
        res = i
res = (res + 1, s[res])
print(*res, sep="\n")
