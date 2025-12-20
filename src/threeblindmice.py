d, sw, *s = (int(input()) for _ in range(5))
res = int(sum(2 * (d / (sw + i)) * i for i in s) + 0.5)
print(res)
