from math import lcm

x, y, n = (int(i) for i in input().split())
l = lcm(x, y)
for i in range(1, n + 1):
    res = "FizzBuzz" if i % l == 0 else "Fizz" if i % x == 0 else "Buzz" if i % y == 0 else i
    print(res)
