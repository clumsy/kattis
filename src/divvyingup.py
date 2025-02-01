n = int(input())
w = (int(i) for i in input().split())
res = "yes" if sum(w) % 3 == 0 else "no"
print(res)
