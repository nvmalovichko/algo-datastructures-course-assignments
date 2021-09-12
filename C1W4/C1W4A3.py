#/usr/bin/python3

import random


def partition3(a, l, r):
    x = a[l]
    m1 = m2 = l
    counter = 1
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
        elif a[i] == x:
            counter += 1
            m2 += 1
            del a[i]
            a.insert(l, x)

    for i in range(counter):
        a.insert(m2 + 1, a[l])
        del a[l]
    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]

    randomized_quick_sort(a, 0, n - 1)
    print(' '.join(str(x) for x in a))
