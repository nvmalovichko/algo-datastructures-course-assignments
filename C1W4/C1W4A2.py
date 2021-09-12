# /usr/bin/python3

from collections import defaultdict


def get_major_element(n, a, left, right, counter):
    if left == right:
        counter[a[left]] += 1
        if counter[a[left]] > n // 2:
            raise BaseException
        else:
            return

    middle = (right - left + 1) // 2

    get_major_element(n, a, left, left + middle - 1, counter)
    get_major_element(n, a, left + middle, right, counter)


def alg_log(n, a):
    if n == 1:
        return 1

    counter = defaultdict(lambda: 0)

    try:
        get_major_element(n, a, 0, n - 1, counter)
        result = 0
    except BaseException:
        result = 1

    return result


def alg_n2(n, a):
    b = sorted(a)
    for i in range(n):
        counter = 0
        x = b[i]
        for j in range(n):
            if b[j] == x:
                counter += 1
        if counter > n // 2:
            return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    a = [int(a) for a in input().split()]
    print(alg_log(n, a))
