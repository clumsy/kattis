_ = input()
a, b, a_b = (int(input()) for i in range(3))
res = "VEIT EKKI" if a_b > 0 and a - b == a_b else "JEDI" if a_b == a - b else "SITH"
print(res)
