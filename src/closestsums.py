try:
    i = 0
    while True:
        n = int(input())
        a = sorted(int(input()) for _ in range(n))
        m = int(input())
        b = (int(input()) for _ in range(m))
        i += 1
        print(f"Case {i}:")
        for k in b:
            lo, hi = 0, n - 1
            res, mi = None, float("inf")
            while lo < hi:
                s = a[lo] + a[hi]
                d = abs(s - k)
                if d < mi:
                    res, mi = s, d
                if s <= k:
                    lo += 1
                else:
                    hi -= 1
            res = f"Closest sum to {k} is {res}."
            print(res)
except:
    pass
