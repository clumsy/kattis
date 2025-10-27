s, d, t = (float(input()) for _ in range(3))
res = "MADE IT" if s * 5280 * t / (60 * 60) >= d else "FAILED TEST"
print(res)
