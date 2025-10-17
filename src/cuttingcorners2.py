from math import sqrt


w, h = (int(i) for i in input().split())
res = w + h - sqrt(w * w + h * h)
print(res)
