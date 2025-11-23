n = int(input())
res = None
for _ in range(n):
    k, r = int(input()), input()
    if len(set(filter(lambda x: x == "pea soup" or x == "pancakes", (input() for _ in range(k))))) > 1:
        res = r
        break
res = res or "Anywhere is fine I guess"
print(res)
