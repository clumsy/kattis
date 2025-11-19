s = input()
h, m = (int(i) for i in input().split(":"))
d = input()
w, s, p = (int(input()) for _ in range(3))
res = h * 60 + m
res = 2 * res if d in "sat|sun" else res
res = 2 * res if w else res
res = 3 * res if s else res
res = 3 * res if p else res
res = ":".join("0" * (e < 10 if i else 0) + str(e) for i, e in enumerate(divmod(res, 60)))
print(res)
