n = int(input())
bs = (input().lower() for _ in range(n))
res = sum("pink" in b or "rose" in b for b in bs) or "I must watch Star Wars with my daughter"
print(res)
