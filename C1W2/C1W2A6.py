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
    period = 60
    fibo_gen = fibo()
    pos = n % period if n > period else n
    result = 0
    for i, x in enumerate(fibo_gen):
        result = (result + x) % 10
        if i == pos:
            return result


n = int(input())
print(foo(n))