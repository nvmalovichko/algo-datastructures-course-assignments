PRIME_N = 100000004987
X = 1  # random.randint(1, PRIME_N - 1)


def poli_hash(text, x, p):
    r = 0
    for i, s in enumerate(text):
        r += (ord(s) * x ** i) % p
    return r % p


def precompute_hashes(text, t_len, p_len, x, p):
    hashed_substrings = [-1 for _ in range(t_len - p_len + 1)]
    last_substr = text[t_len - p_len:t_len]
    hashed_substrings[t_len - p_len] = poli_hash(last_substr, x, p)

    y = 1
    for _ in range(p_len):
        y = (y * x) % p

    for i in range(t_len - p_len)[::-1]:
        hashed_substrings[i] = (x * hashed_substrings[i + 1] + ord(text[i]) - y * ord(text[i + p_len])) % p
    return hashed_substrings


def find(pattern, text):
    t_len = len(text)
    p_len = len(pattern)
    prehash = precompute_hashes(text, t_len, p_len, X, PRIME_N)

    p_hash = poli_hash(pattern, X, PRIME_N)
    for i in range(t_len - p_len + 1):
        if p_hash != prehash[i]:
            continue
        if pattern == text[i:(i + p_len)]:
            yield i


if __name__ == '__main__':
    # print(list(find('aba', 'abacaba')))
    # print(list(find('Test', 'testTesttesT')))
    # print(list(find('aaaaa', 'baaaaaaa')))
    #
    # t1 = time.time()
    # print(list(find('abaab' * 10, 'abaab' * 1000000)))
    # print(time.time() - t1)

    print(' '.join(str(x) for x in find(input(), input())))
