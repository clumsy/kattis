a, b = (int(i) for i in input().split())
a, b = min(a, b), max(a, b)
n, k = int(input()), 0
for _ in range(n):
    ai = int(input())
    k += a < ai < b
res = (b - a) * 4 + k * 10
print(res)
