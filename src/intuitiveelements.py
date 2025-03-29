n = int(input())
for _ in range(n):
    a, b = (input() for _ in range(2))
    res = "YES" if set(a) & set(b) == set(b) else "NO"
    print(res)
