while True:
    n = int(input())
    if n < 0:
        break
    res = t_ = 0
    for _ in range(n):
        s, t = (int(i) for i in input().split())
        res += s * (t - t_)
        t_ = t
    res = f"{res} miles"
    print(res)
