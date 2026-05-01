n, m = input().split()
res = 0
while m:
    m_, r = [], 0
    for d in m:
        d, r = divmod(r * 10 + int(d), 2)
        if d != 0 or len(m_) > 0:
            m_.append(str(d))
    res += r > 0
    m = m_
print(res)
