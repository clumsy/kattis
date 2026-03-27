while True:
    f, s = input().strip(), input().strip()
    if f == s == "E":
        break
    p1 = p2 = 0
    for i, j in zip(f, s):
        c = 0 if i == j else 1 if (i == "R" and j == "S") or (i == "S" and j == "P") or (i == "P" and j == "R") else -1
        p1 += c > 0
        p2 += c < 0
    res = f"P1: {p1}\nP2: {p2}"
    print(res)
