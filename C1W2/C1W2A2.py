#/usr/bin/python3


def foo(n):
    counter = 2
    a = 0
    b = 1
    if n <= 1:
        return n
    else:
        while n >= counter:
            c = (a + b) % 10
            a, b = b, c
            counter += 1
        return c


n = int(input())
print(foo(n))