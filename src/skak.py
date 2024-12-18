x_h, y_h = (int(i) for i in input().split())
x_p, y_p = (int(i) for i in input().split())
res = 1 if y_h == y_p or x_h == x_p else 2
print(res)
