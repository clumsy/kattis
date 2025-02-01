g, s, c = (int(i) for i in input().split())
res = []
b = c + 2 * s + 3 * g
res = [] if b < 2 else ["Estate"] if b < 5 else ["Duchy"] if b < 8 else ["Province"]
res.append("Gold" if b >= 6 else "Silver" if b >= 3 else "Copper")
res = " or ".join(res)
print(res)
