n = int(input())
a = [input() for _ in range(n)]
res = "INCREASING" if a == sorted(a) else "DECREASING" if a[::-1] == sorted(a) else "NEITHER"
print(res)
