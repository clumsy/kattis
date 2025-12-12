n = int(input())
res, dir = set(), []
for _ in range(n):
    c, t = input().split()
    if c == "cd":
        if t == "..":
            dir.pop()
        else:
            dir.append(t)
    else:
        file = "/".join([*dir, t])
        res.add(f"git add {file}")
res = sorted(res)
res.append("git commit")
res.append("git push")
print(*res, sep="\n")
