from math import pow


while True:
    s = input()
    if s == "0":
        break
    x1, y1, x2, y2, p = (float(f) for f in s.split())
    res = pow(pow(abs(x1 - x2), p) + pow(abs(y1 - y2), p), 1 / p)
    print(res)
