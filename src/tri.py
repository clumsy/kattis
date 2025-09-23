a, b, c = (int(i) for i in input().split())
res = (
    f"{a}+{b}={c}" if a + b == c else
    f"{a}-{b}={c}" if a - b == c else
    f"{a}*{b}={c}" if a * b == c else
    f"{a}/{b}={c}" if a // b == c else
    f"{a}={b}+{c}" if a == b + c else
    f"{a}={b}-{c}" if a == b - c else
    f"{a}={b}*{c}" if a == b * c else
    f"{a}={b}/{c}"
)
print(res)
