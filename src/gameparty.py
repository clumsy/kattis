g = int(input())
s = (int(i) for i in input().split())
res = (sum(s) + 1) % 3
print(res)
