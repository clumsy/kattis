y = {
    ".": 20,
    "O": 10,
    "\\": 25,
    "/": 25,
    "A": 35,
    "^": 5,
    "v": 22,
}
n, m = (int(i) for i in input().split())
res = 0
for _ in range(n):
    s = input()
    res += sum(y[c] for c in s)
print(res)
