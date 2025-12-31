# hour arrow angle is M // 60 * (360 / 12) + (M % 60 / 60) * (360 / 12)
# minute arrow angle is M % 60 * (360 / 60)
a = int(input())
# a = M % 60 * 6 - 30 * (M // 60 + M % 60 / 60) = M % 60 * 5.5 - 30 * M // 60
for m in range(12 * 60):
    d = 55 * (m % 60) - 300 * (m // 60)
    d = d if d >= 0 else 3600 + d
    if a == d:
        h, m = m // 60, m % 60
        res = f"{h:02d}:{m:02d}"
        break
print(res)
