n = int(input())
a = (int(i) for i in input().split())
res = -sum(i for i in a if i < 0)
print(res)
