y = ny = 0
s = input()
for c in s:
    if c in "aeoiu":
        ny += 1
    elif c == "y":
        y += 1
res = ny, ny + y
print(*res)
