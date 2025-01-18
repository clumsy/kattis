n = int(input())
for i in range(5):
    if i % 2 == 1 or i % 4 == 0:
        res = "  " + " ".join(("|" if i % 2 == 1 else "H") * n)
    else:
        res = "H-" + "-".join("C" * n) + "-OH"
    print(res)
