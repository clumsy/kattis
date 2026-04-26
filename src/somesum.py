n = int(input())
res = "Odd" if n % 4 == 2 else "Even" if n & 1 == 0 else "Either"
print(res)
