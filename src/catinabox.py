h, w, l, c = (int(i) for i in input().split())
d = h * w * l - c
res = "TOO TIGHT" if d < 0 else "COZY" if d == 0 else "SO MUCH SPACE"
print(res)

