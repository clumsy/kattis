x, y, z = (int(i) for i in input().split())
res = (x + y + 2 * z) / 4
res = "A" if res >= 90 else "B" if res >= 80 else "C" if res >= 70 else "D" if res >= 60 else "F"
print(res)
