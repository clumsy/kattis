h, k, v, s = (int(i) for i in input().split())
res = 0
while h > 0:
    v += s
    v -= max(1, v // 10)
    if v >= k:
        h += 1
    elif 0 < v < k:
        h -= 1
        v = 0 if h == 0 else v
    else:
        h = v = 0
    res += v
    s = max(0, s - 1)
print(res)
