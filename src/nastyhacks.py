t = int(input())
for _ in range(t):
    da, a, c = (int(i) for i in input().split())
    res = "advertise" if a - c > da else "does not matter" if a - c == da else "do not advertise"
    print(res)
