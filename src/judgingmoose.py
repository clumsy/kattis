l, r = (int(i) for i in input().split())
d, c = "Even" if l == r else "Odd", max(l, r)
res = f"{d} {2 * c}" if c > 0 else "Not a moose"
print(res)
