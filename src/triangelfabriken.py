a, b, c = (int(input()) for _ in range(3))
res = "Ratvinklig Triangel" if any(i == 90 for i in (a, b, c)) else "Spetsig Triangel" if max(a, b, c) > 90 else "Trubbig Triangel"
print(res)
