# /usr/bin/python3


def bin_search(search_in, value, left=0, right=None):
    right = len(search_in) - 1 if right is None else right

    search_length = right - left + 1

    if search_length == 0:
        return -1

    mid_number = search_length // 2
    mid_index = mid_number + left
    mid_value = search_in[mid_index]

    if value == mid_value:
        return mid_index
    elif value <= mid_value:
        return bin_search(search_in, value, left, mid_index - 1)
    elif value > mid_value:
        return bin_search(search_in, value, mid_index + 1, right)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    a_len, *a_list = [int(x) for x in input().split()]
    b_len, *b_list = [int(x) for x in input().split()]

    for b in b_list:
        print(bin_search(a_list, b), end=' ')

    # for _ in range(1000):
    #     print(_)
    #     a_len = random.randint(1, 30000000000)
    #     a_array = sorted(i + 1 for i in range(a_len))
    #
    #     b_len = random.randint(1, 100)
    #     b_array = [random.randint(1, 10000000000) for _ in range(b_len)]
    #
    #     result1 = []
    #     for b in b_array:
    #         result1.append(str(bin_search(a_array, b, 0, int(a_len) - 1)))
    #     result1 = ' '.join(result1)
    #
    #
    #     result2 = []
    #     for b in b_array:
    #         result2.append(str(linear_search(a_array, b)))
    #     result2 = ' '.join(result2)
    #
    #     assert result1 == result2
