from math import gcd


n = int(input())
a = (int(i) for i in input().split())
f = next(a)
for i in a:
    g = gcd(f, i)
    res = f"{f // g}/{i // g}"
    print(res)
    f = i // (i // g) * (f // g)
