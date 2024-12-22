n = int(input())
a = (int(i) for i in input().split())
res = sum(i < 0 for i in a)
print(res)
