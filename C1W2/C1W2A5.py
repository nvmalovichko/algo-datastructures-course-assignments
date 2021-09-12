#/usr/bin/python3


def fibo():
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a, b = b, c


def find_period(mod):
    fibo_gen = fibo()
    last_array = [-1, -1]
    count_period = 0
    counter = 0

    while count_period < 2:
        counter += 1
        f = next(fibo_gen)
        res = f % mod
        last_array[0], last_array[1] = last_array[1], res
        if last_array == [0, 1]:
            count_period += 1
    return counter - 2
                 

def foo(n, m):
    period = find_period(m)
    fibo_gen = fibo()
    pos = n % period if n > period else n
    for i, x in enumerate(fibo_gen):
        if i == pos:
            return x % m


n, mod = [int(x) for x in input().split()]
print(foo(n, mod))

