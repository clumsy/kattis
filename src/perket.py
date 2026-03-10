n = int(input())
s, b = [1] * (1 << n), [0] * (1 << n)
for x in range(n):
    s_, b_ = (int(i) for i in input().split())
    for i in range(1 << n):
        if i & (1 << x) == (1 << x):
            s[i] *= s_
            b[i] += b_

res = float("inf")
for i in range(1, 1 << n):
    res = min(res, abs(s[i] - b[i]))
print(res)
