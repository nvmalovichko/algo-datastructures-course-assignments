#/usr/bin/python3


def fibo():
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = (a + b) % 10
        yield c
        a, b = b, c


def foo(n):
    period = 60
    pos = n % period if n > period else n
    for i, x in enumerate(fibo()):
        if i == pos:
            pos_x = x
        if i == pos + 1:
            return (pos_x * x) % 10
        

n = int(input())
print(foo(n))