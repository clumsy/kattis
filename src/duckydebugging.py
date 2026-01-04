while True:
    s = input()
    if s == "I quacked the code!":
        break
    res = "Quack!" if s[-1] == "?" else "*Nod*"
    print(res)
