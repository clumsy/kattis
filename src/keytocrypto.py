from string import ascii_uppercase


c, k = (input() for _ in range(2))
res = [None] * len(c)
for i, e in enumerate(c):
    d = (ord(e) - ord(k[i] if i < len(k) else res[i - len(k)])) % 26
    res[i] = ascii_uppercase[d]

res = "".join(res)
print(res)
