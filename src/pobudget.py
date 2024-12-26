n = int(input())
e = ((input(), int(input())) for _ in range(n))
res = sum(v for _, v in e)
res = "Usch, vinst" if res > 0 else "Lagom" if res == 0 else "Nekad"
print(res)
