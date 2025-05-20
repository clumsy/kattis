n, m = (int(i) for i in input().split())
d = "s" if abs(n - m) > 1 else ""
res = f"Dr. Chaz will have {m - n} piece{d} of chicken left over!" if m - n > 0 else f"Dr. Chaz needs {n - m} more piece{d} of chicken!"
print(res)
