x, y = (int(input()) for _ in range(2))
res = 1 if x > 0 and y > 0 else \
      2 if y > 0 and x < 0 else \
      3 if x < 0 and y < 0 else 4
print(res)
