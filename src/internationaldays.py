s = [int(i) for i in input().split("/")]
res = "US" if s[1] > 12 else "EU" if s[0] > 12 else "either"
print(res)
