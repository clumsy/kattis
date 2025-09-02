n = int(input())
res = 0
for _ in range(n):
    s = input()
    res += s.startswith("+39") and 9 <= len(s) - 3 <= 10
print(res)
