n = int(input())
res = []
for i in range(2, (n + 1) // 2 + 1):
    if n % (i + i - 1) in [0, i]:
        res.append(f"{i},{i - 1}")
    if n % i == 0:
        res.append(f"{i},{i}")
print(f"{n}:")    
print(*res, sep="\n")
