n = int(input())
a = [int(input()) for _ in range(n)]
res = reversed(a)
print(*res, sep="\n")
