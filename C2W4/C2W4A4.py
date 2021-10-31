import random

M1 = int(1e9) + 7
M2 = int(1e9) + 9
X = random.randint(1, pow(10, 9))

PREFIX_HASHES_1, PREFIX_HASHES_2 = [0], [0]
POW_1, POW_2 = [X], [X]


def substr_hash(prehash, s_len, position, p, pow_list):
    return (prehash[position + s_len] - (pow_list[s_len - 1] * prehash[position]) % p) % p


def precompute(text, x, p1, p2):
    for i, s in enumerate(text, 1):
        PREFIX_HASHES_1.append(((x * PREFIX_HASHES_1[i - 1]) % p1 + ord(s)) % p1)
        PREFIX_HASHES_2.append(((x * PREFIX_HASHES_2[i - 1]) % p2 + ord(s)) % p2)
        POW_1.append((POW_1[i - 1] * x) % p1)
        POW_2.append((POW_2[i - 1] * x) % p2)


def is_equal(p_index_1, p_index_2, p_len):
    h_substr_1_m1 = substr_hash(prehash=PREFIX_HASHES_1, s_len=p_len, p=M1, pow_list=POW_1, position=p_index_1)
    h_substr_1_m2 = substr_hash(prehash=PREFIX_HASHES_2, s_len=p_len, p=M2, pow_list=POW_2, position=p_index_1)

    h_substr_2_m1 = substr_hash(prehash=PREFIX_HASHES_1, s_len=p_len, p=M1, pow_list=POW_1, position=p_index_2)
    h_substr_2_m2 = substr_hash(prehash=PREFIX_HASHES_2, s_len=p_len, p=M2, pow_list=POW_2, position=p_index_2)

    if h_substr_1_m1 == h_substr_2_m1 and h_substr_1_m2 == h_substr_2_m2:
        return 'Yes'
    else:
        return 'No'


def run():
    text = input()
    command_n = int(input())
    results = []
    precompute(text, X, M1, M2)

    for _ in range(command_n):
        index_1, index_2, p_len = [int(x) for x in input().split()]
        results.append(is_equal(index_1, index_2, p_len))
    return results


def run_test(text, inputs):
    results = []
    precompute(text, X, M1, M2)

    for inp in inputs:
        index_1, index_2, p_len = inp
        results.append(is_equal(index_1, index_2, p_len))
    return results


if __name__ == '__main__':
    # print(run_test('trololo',
    #                [(6, 6, 1),
    #                 (0, 0, 7),
    #                 (2, 4, 3),
    #                 (3, 5, 1),
    #                 (1, 3, 2)]))
    # print(run_test('abacabadabacaba',
    #                [(0, 0, 1),
    #                 (0, 0, 2),
    #                 (0, 0, 3),
    #                 (0, 0, 4),
    #                 (0, 0, 5),
    #                 (0, 0, 15)]))

    for r in run():
        print(r)
