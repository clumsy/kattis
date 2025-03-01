n = int(input())
for _ in range(n):
    s = input()
    if s == "P=NP":
        res = "skipped"
    else:
        a, b = (int(i) for i in s.split("+"))
        res = a + b
    print(res)
