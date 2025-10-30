a = (int(i) for i in input().split())
cnt = [0] * 10
for i in a:
    res = i % 10
res = res or 10
print(res)
