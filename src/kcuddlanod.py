n, m = (int(i[::-1]) for i in input().replace("2", "X").replace("5", "2").replace("X", "5").split())
res = 1 if n > m else 2
print(res)
