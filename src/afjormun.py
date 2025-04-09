n = int(input())
for _ in range(n):
    s = input()
    res = s[0].upper() + s[1:].lower()
    print(res)
