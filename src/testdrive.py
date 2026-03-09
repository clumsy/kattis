a, b, c = (int(i) for i in input().split())
d1, d2 = b - a, c - b
res = "turned" if d1 * d2 < 0 else "cruised" if d1 == d2 else "accelerated" if abs(d2) > abs(d1) else "braked"
print(res)
