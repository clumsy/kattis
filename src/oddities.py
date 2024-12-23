n = int(input())
for _ in range(n):
    x = int(input())
    res = "odd" if x & 1 == 1 else "even"
    print(f"{x} is {res}")
