n = int(input())
gs = set()
for _ in range(n):
    s, g = input().split()
    if s == "+":
        gs.add(g)
    elif s == "-":
        gs.remove(g)
    else:
        res = "Jebb" if g in gs else "Neibb"
        print(res)
