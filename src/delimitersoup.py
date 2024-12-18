n, s = int(input()), input()
st = []
res = "ok so far"
for i, c in enumerate(s):
    if c in "([{":
        st.append(c)
    elif c in "}])":
        p = "{" if c == "}" else "[" if c == "]" else "("
        if not st or st[-1] != p:
            res = f"{c} {i}"
            break
        st.pop()
print(res)
