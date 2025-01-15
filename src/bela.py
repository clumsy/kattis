n, b = input().split()
def value(i):
    v, s = i
    if v in "AKQT87":
        return 11 if v == "A" else 4 if v == "K" else 3 if v == "Q" else 10 if v == "T" else 0
    if s == b:
        return 14 if v == "9" else 20
    return 2 if v == "J" else 0
res = sum(value(input()) for _ in range(4 * int(n)))
print(res)
