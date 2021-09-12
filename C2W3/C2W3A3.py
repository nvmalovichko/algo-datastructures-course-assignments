from collections import deque
from functools import lru_cache


@lru_cache()
def hash_it(text):
    p = 1000000007
    x = 263

    r = 0
    for i, s in enumerate(text):
        r += (ord(s) * x ** i)
    return r % p

def are_equal(p, s):
    return p == s

def find(pattern, text):
    pass


if __name__ == '__main__':
    find(input(), input())
