m, n = (int(input()) for _ in range(2))
empty = 0
for _ in range(n):
    s = input()
    empty += s.count(".")
res = empty / (m * n)
print(res)
