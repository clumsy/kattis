s, p, n = input(), float(input()), int(input())
c = (input() for _ in range(n))
res = "Jebb" if sum(i == "plast" for i in c) / n >= (1 - p) else "Neibb"
print(res)
