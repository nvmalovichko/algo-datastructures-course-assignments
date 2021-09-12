#/usr/bin/python3


def foo(m, n):
    if m == n:
        return m

    l = 1
    counter = 2
    maxi, mini = m, n
    while True:
        if counter > mini:
            break
        maxi_ = maxi % counter
        mini_ = mini % counter
        if not maxi_ and not mini_:
            l *= counter
            maxi, mini = maxi / counter, mini / counter
        else:
            counter += 1
    return m * n / l

        
numbers = [int(x) for x in input().split()]
maxi, mini = max(numbers), min(numbers)
print(int(foo(maxi, mini)))