n = int(input())
m = [input() for _ in range(n)]
res = m[0] if n == 1 or m[0] == m[1] else "blandad best"
print(res)
