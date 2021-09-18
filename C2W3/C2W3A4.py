import functools
import random

M1 = 10 ** 9 + 7
M2 = 10 ** 9 + 9
X = random.randint(1, 10 ** 9)


def substr_hash(prehash, s_len, position, x, p):
    return (prehash[position + s_len] - x ** s_len * prehash[position]) % p


def precompute_hashes(text, t_len, x, p):
    prefix_hashes = [-1 for _ in range(t_len + 1)]
    prefix_hashes[0] = 0
    for i, s in enumerate(text, 1):
        prefix_hashes[i] = (x * prefix_hashes[i - 1] + ord(s)) % p
    return prefix_hashes


def is_equal(p_index_1, p_index_2, p_len, text):
    t_len = len(text)
    prefix_hashes_1 = precompute_hashes(text, t_len, X, M1)
    prefix_hashes_2 = precompute_hashes(text, t_len, X, M2)

    hash_func_1 = functools.partial(substr_hash, prehash=prefix_hashes_1, s_len=p_len, x=X, p=M1)
    hash_func_2 = functools.partial(substr_hash, prehash=prefix_hashes_2, s_len=p_len, x=X, p=M2)

    if (hash_func_1(position=p_index_1) == hash_func_1(position=p_index_2) and
            hash_func_2(position=p_index_1) == hash_func_2(position=p_index_2)):
        return 'Yes'
    else:
        return 'No'


def run():
    text = input()
    command_n = int(input())
    results = []
    inputs = []
    for _ in range(command_n):
        inputs.append([int(x) for x in input().split()])
    for inp in inputs:
        index_1, index_2, p_len = inp
        results.append(is_equal(index_1, index_2, p_len, text))
    return results


def run_test(text, inputs):
    results = []
    for inp in inputs:
        index_1, index_2, p_len = inp
        results.append(is_equal(index_1, index_2, p_len, text))
    return results


if __name__ == '__main__':
    # print(run_test('trololo', [(6, 6, 1), (0, 0, 7), (2, 4, 3), (3, 5, 1), (1, 3, 2)]))

    for r in run():
        print(r)
