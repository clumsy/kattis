n = int(input())
res = 0
for _ in range(n):
    p = input()
    res += int(int(p[:-1]) ** int(p[-1:]))
print(res)
