n, m = (int(i) for i in input().split())
s = [input() for _ in range(n)]
res = []
for i in range(m):
    cnt = [0] * 26
    ma = 0
    for j in range(n):
        c = ord(s[j][i]) - ord("a")
        cnt[c] += 1
        if cnt[c] > cnt[ma] or (cnt[c] == cnt[ma] and ma > c):
            ma = c
    res.append(chr(ord("a") + ma))
res = "".join(res)
print(res)
