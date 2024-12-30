n = int(input())
res = 0
p = None
for _ in range(n):
    s = input()
    if p != "drunk" and s == "drunk":
        res += 1
    p = s
print(res)
