#/usr/bin/python3


def foo(n1, n2):
    n3 = n1 % n2
    return foo(n2, n3) if n3 else n2


numbers = [int(x) for x in input().split()]
n1, n2 = max(numbers), min(numbers)
print(foo(n1, n2))