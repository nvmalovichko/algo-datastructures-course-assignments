#/usr/bin/python3


def fibo():
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c % 10
        a, b = b, c
                 

def foo(m, n):
    period = 60
    fibo_gen = fibo()
    pos_m = m % period if m > period else m
    pos_n = n % period if n > period else n
    if pos_m > pos_n:
        pos_n += period
    result = 0
    for i, x in enumerate(fibo_gen):
        add = x if i >= pos_m else 0
        result = (result + add) % 10
        if i == pos_n:
            return result


m, n = [int(x) for x in input().split()]
print(foo(m, n))