n = int(input())
res = 7
for _ in range(n):
    s = input()
    res = max(0, min(10, res + (1 if s == "Skru op!" else -1)))
print(res)
