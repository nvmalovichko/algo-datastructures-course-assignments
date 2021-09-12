from functools import lru_cache


@lru_cache()
def poli_hash(text):
    prime_n = 250000000007
    x = 263

    r = 0
    for i, s in enumerate(text):
        r += (ord(s) * x ** i)
    return r % prime_n


def find(pattern, text):
    t_len = len(text)
    p_len = len(pattern)
    p_hash = poli_hash(pattern)
    for i in range(t_len - p_len + 1):
        substring = text[i:(i + p_len)]
        if p_hash != poli_hash(substring):
            continue
        if pattern == substring:
            yield i


if __name__ == '__main__':
    # print(list(find('aba', 'abacaba')))
    # print(list(find('Test', 'testTesttesT')))
    # print(list(find('aaaaa', 'baaaaaaa')))

    print(' '.join(str(x) for x in find(input(), input())))
