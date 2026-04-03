n, s = int(input()), input()
for i in reversed(range(n)):
    if i != n - 1:
        print()
    v = "one" if i else "it"
    t = i + 1
    te = "s" if t != 1 else ""
    t_ = i if i else "no more"
    te_ = "s" if t - 1 != 1 else ""
    e = " on the wall" if i else ""
    res = f"{t} bottle{te} of {s} on the wall, {t} bottle{te} of {s}.\nTake {v} down, pass it around, {t_} bottle{te_} of {s}{e}."
    print(res)
