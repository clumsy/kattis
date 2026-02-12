n = int(input())
m = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
m = {c: v for v, s in m.items() for c in s}
for _ in range(n):
    s = input()
    res = "".join(m[c] for c in s.lower())
    print(res)
