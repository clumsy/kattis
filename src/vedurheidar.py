v, n = (int(input()) for _ in range(2))
k = (int(input()) for _ in range(n))
for _ in range(n):
    s, k = input().split()
    res = "lokud" if v > int(k) else "opin"
    res = f"{s} {res}"
    print(res)
