s = input().split()
res = (sum("ae" in c for c in s) * 100) // len(s) >= 40
res = "dae ae ju traeligt va" if res else "haer talar vi rikssvenska"
print(res)
