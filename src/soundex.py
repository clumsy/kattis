try:
    m = [" ", "BFPV", "CGJKQSXZ", "DT", "L", "MN", "R"]
    m = {c: str(i) for i, s in enumerate(m) for c in s}
    while True:
        s = input()
        st = []
        for c in s:
            v = m.get(c, "")
            if not st or st[-1] != v:
                st.append(v)
        res = "".join(st)
        print(res)
except:
    pass
