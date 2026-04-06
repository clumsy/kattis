from itertools import combinations as comb
from itertools import permutations as perm


def valid(d, m, y):
    if int(y) < 2000 or len(d) != 2 or len(m) != 2:
        return False
    d, m, y = (int(i) for i in (d, m, y))
    if m < 1 or m > 12 or d < 1:
        return False
    if (m in {4, 6, 9, 11} and d > 30) or (m not in {4, 6, 9, 11} and d > 31):
        return False
    if m == 2 and (d > 29 or (d == 29 and not (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)))):
        return False
    return True


n = int(input())
for _ in range(n):
    cnt = set()
    mi = ("9999", "99", "99")
    s = input().replace(" ", "")
    rem_d = range(len(s))
    for d_id in comb(rem_d, 2):
        rem_m = [i for i in rem_d if i not in d_id]
        for m_id in comb(rem_m, 2):
            dd = [s[i] for i in d_id]
            md = [s[i] for i in m_id]
            yd = [s[i] for i in rem_m if i not in m_id]
            for d in set(perm(dd)):
                for m in set(perm(md)):
                    for y in set(perm(yd)):
                        d_ = "".join(d)
                        m_ = "".join(m)
                        y_ = "".join(y)
                        if valid(d_, m_, y_):
                            cnt.add((d_, m_, y_))
                            mi = min(mi, (y_, m_, d_))
    res = (len(cnt), f"{mi[2]} {mi[1]} {mi[0]}") if cnt else [0]
    print(*res)
