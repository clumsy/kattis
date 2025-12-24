n = int(input())
res = []
for _ in range(n):
    s = input()
    if s == "Present!":
        res.pop()
    else:
        res.append(s)
res = res or ["No Absences"]
print(*res, sep="\n")
