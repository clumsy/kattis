s = input()
n = len(s)
i = k = 1
while i < n:
    d, r = divmod(n, i)
    k = i if r == 0 and i <= d else k
    i += 1
res = "".join(s[r + c * k] for r in range(k) for c in range(n // k))
print(res)
