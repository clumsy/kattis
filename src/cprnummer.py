c = input().replace("-", "")
res = 1 if sum(i * int(ci) for i, ci in zip((4, 3, 2, 7, 6, 5, 4, 3, 2, 1), c)) % 11 == 0 else 0
print(res)
