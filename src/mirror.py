t = int(input())
for i in range(t):
    r, c = (int(i) for i in input().split())
    g = [input() for _ in range(r)]
    res = [r[::-1] for r in g[::-1]]
    print(f"Test {i + 1}")
    for r in res:
        print(r)
