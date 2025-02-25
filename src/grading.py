a, b, c, d, e = (int(i) for i in input().split())
s = int(input())
res = "A" if s >= a else "B" if s >= b else "C" if s >= c else "D" if s >= d else "E" if s >= e else "F"
print(res)
