#/usr/bin/python3


def fibo():
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a, b = b, c


def foo(n):
    for i, x in enumerate(fibo()):
        if i == n:
            return x


n = int(input())
print(foo(n))