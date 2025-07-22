n = int(input())
w = [input() for _ in range(n)]
res = []
for i in range(max(len(wi) for wi in w)):
    cur = cnt = 0
    for j in range(n):
        if len(w[j]) >= i + 1:
            cur += ord(w[j][i])
            cnt += 1
    res.append(chr(cur // cnt))
res = "".join(res)
print(res)
