import sys


for i, s in enumerate(sys.stdin):
    n, *a = (int(i) for i in s.split())
    mi, ma = float("inf"), float("-inf")
    for e in a:
        mi = min(mi, e)
        ma = max(ma, e)
    res = mi, ma, ma - mi
    print(f"Case {i + 1}:", *res)
