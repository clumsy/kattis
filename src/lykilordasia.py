s = input()
res = []
for c in s + " ":
    if c == " ":
        st = []
        has_d = has_l = False
        while res and res[-1] != " ":
            has_d |= res[-1].isdigit()
            has_l |= res[-1].isalpha()
            st.append(res.pop())
        res.append("*" * len(st) if has_d and has_l else "".join(st[::-1]))
    res.append(c)
res = "".join(res[:-1])
print(res)
