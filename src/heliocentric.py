try:
    i = 0
    while True:
        i += 1
        e, m = (int(i) for i in input().split())
        # (a + x)%365 = (b + x)%687
        res = x = 0
        while not res:
            if (e + x) % 365 == (m + x) % 687:
                res = f"Case {i}: {x}"
            x += 1
        print(res)
except:
    pass
