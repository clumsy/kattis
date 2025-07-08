t = int(input())
for i in range(t):
    n = int(input())
    a = sorted(int(i) for i in input().split())
    b = sorted((int(i) for i in input().split()), reverse=True)
    res = sum(ai * bi for ai, bi in zip(a, b))
    print(f"Case #{i + 1}: {res}")
