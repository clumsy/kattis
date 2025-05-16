s = input()
n = len(s)
s = s[:n // 2], s[n // 2:]
r = [sum(ord(c) - ord("A") for c in ch) for ch in s]
def rotate(s, i):
    return "".join(chr(ord("A") + (ord(c) - ord("A") + i) % 26) for c in s)
r = [rotate(si, ri) for si, ri in zip(s, r)]
res = "".join(rotate(si, ord(ci) - ord("A")) for si, ci in zip(*r))
print(res)
