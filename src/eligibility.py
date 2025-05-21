n = int(input())
for _ in range(n):
    n, dp, db, nc = input().split()
    dp = int(dp[:4])
    db = int(db[:4])
    nc = int(nc)
    res = "eligible" if dp >= 2010 or db >= 1991 else "ineligible" if nc > 40 else "coach petitions"
    res = f"{n} {res}"
    print(res)
