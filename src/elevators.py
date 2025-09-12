s, n = input().split()
n = int(n)
if s == "residential":
    res = 0 if n < 2 else 1 if n < 6 else 2 if n < 11 else 3 if n < 16 else 4
elif s == "commercial":
    res = 0 if n < 2 else 1 if n < 8 else 2 if n < 15 else 3
else:
    res = 0 if n < 2 else 1 if n < 5 else 2 if n < 9 else 3 if n < 13 else 4 if n < 17 else 5
print(res)
