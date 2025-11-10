while True:
    m = int(input())
    if not m:
        break
    tw = th = ch = 0
    cw = m
    while True:
        w, h = (int(i) for i in input().split())
        if w == h == -1:
            break
        if cw + w > m:
            th += ch
            cw = ch = 0
        ch = max(ch, h)
        cw += w
        tw = max(tw, cw)
    th += ch
    res = f"{tw} x {th}"
    print(res)
