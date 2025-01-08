n = int(input())
for _ in range(n):
    s = input()
    if s.startswith("Simon says"):
        res = s[len("Simon says"):]
        print(res)
