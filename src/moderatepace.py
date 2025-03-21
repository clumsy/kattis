n = int(input())
a = (int(i) for i in input().split())
b = (int(i) for i in input().split())
c = (int(i) for i in input().split())
res = [sorted([i, j, k])[1] for i, j, k in zip(a, b, c)]
print(*res)
