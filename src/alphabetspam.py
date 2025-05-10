s = input()
cnt = [0] * 4
for c in s:
    if c == "_":
        cnt[0] += 1
    elif c.islower():
        cnt[1] += 1
    elif c.isupper():
        cnt[2] += 1
    else:
        cnt[3] += 1
n = len(s)
res = [i / n for i in cnt]
print(*res, sep="\n")
