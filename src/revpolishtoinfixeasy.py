s = input().split()
q = []
for c in s:
    if c in "-+*/":
        a, b = q.pop(), q.pop()
        c = f"({b}{c}{a})"
    q.append(c)
res = q.pop()
print(res)
