n = int(input())
d = (int(input()) for _ in range(n))
res = sum(i & 1 for i in d)
print(res)
