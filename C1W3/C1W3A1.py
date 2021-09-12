#/usr/bin/python3


def foo(m):
    result = 0
    coins = (10, 5, 1)
    for value in coins:
        number = m // value
        if number > 0:
            m -= value * number
            result += number
    return result


m = int(input())
print(foo(m))