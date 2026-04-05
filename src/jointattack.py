from math import gcd


n = int(input())
a = [int(i) for i in input().split()]
t, b = 1, a.pop()
while a:
    x = a.pop()
    b, t = t + x * b, b
g = gcd(t, b)
res = f"{b // g}/{t // g}"
print(res)
