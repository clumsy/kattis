t, s = (input() for _ in range(2))
t, s, r = set(t), list(s[::-1]), 10
while t and r > 0:
    if s[-1] not in t:
        r -= 1
    else:
        t.remove(s[-1])
    s.pop()
res = "WIN" if not t else "LOSE"
print(res)
