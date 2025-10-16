n = int(input())
ins = set()
for _ in range(n):
    t, p = input().split()
    if t == "entry":
        res = " (ANOMALY)" if p in ins else ""
        ins.add(p)
        t = "entered"
    else:
        res = " (ANOMALY)" if p not in ins else ""
        if p in ins:
            ins.remove(p)
        t = "exited"
    print(f"{p} {t}{res}")
