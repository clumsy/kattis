n = int(input())
ta, da = (int(i) for i in input().split())
tb, db = (int(i) for i in input().split())
d = (ta + ta + (n - 1) * da) * n // 2 - (tb + tb + (n - 1) * db) * n // 2
res = "Alice" if d < 0 else "Bob" if d > 0 else "="
print(res)
