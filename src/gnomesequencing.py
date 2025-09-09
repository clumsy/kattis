n = int(input())
print("Gnomes:")
for _ in range(n):
    a, b, c = (int(i) for i in input().split())
    res = "Ordered" if a <= b <= c or a >= b >= c else "Unordered"
    print(res)
