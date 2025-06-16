n = int(input())
res = True
for _ in range(3):
    res &= "7" in input().split()
res = 777 if res else 0
print(res)
