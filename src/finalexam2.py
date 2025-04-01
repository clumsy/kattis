n = int(input())
s = "".join(input() for _ in range(n))
res = sum(l == r for l, r in zip(s[:-1], s[1:]))
print(res)
