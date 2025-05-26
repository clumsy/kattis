a, done = [int(i) for i in input().split()], False
while not done:
    done = True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            print(*a)
            done = False
