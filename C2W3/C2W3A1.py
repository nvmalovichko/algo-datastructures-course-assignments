import math


def get_parent_index(i):
    return (i - 1) // 2


def get_left_child_index(i):
    return i * 2 + 1


def get_right_child_index(i):
    return i * 2 + 2


def last_not_leave_index(n):
    return (n // 2) - 1


def sift_down(n, ar, i, swaps, last_node_index):
    left_index = get_left_child_index(i)
    right_index = get_right_child_index(i)

    parent = (ar[i], i)
    child_left = (ar[left_index], left_index)
    if right_index <= n - 1:
        child_right = (ar[right_index], right_index)
    else:
        child_right = (math.inf, -1)
    min_item = min((parent, child_left, child_right), key=lambda x: x[0])
    if min_item != parent:
        swaps.append((parent[1], min_item[1]))
        ar[i], ar[min_item[1]] = ar[min_item[1]], ar[i]

    if left_index <= last_node_index:
        sift_down(n, ar, left_index, swaps, last_node_index)
    if right_index != -1 and right_index <= last_node_index:
        sift_down(n, ar, right_index, swaps, last_node_index)


def build_heap(n, ar):
    swaps = list()

    if n == 1:
        return swaps

    last_node_index = last_not_leave_index(n)
    not_leaves_indexes = list(reversed(range(last_node_index + 1)))
    for i in not_leaves_indexes:
        sift_down(n, ar, i, swaps, last_node_index)
    return swaps


if __name__ == '__main__':
    n = int(input())
    ar = [int(x) for x in input().split()]
    swaps = build_heap(n, ar)

    swaps_n = len(swaps)
    print(swaps_n)
    # print(ar)

    if swaps_n > 0:
        for x, y in swaps:
            print(f'{x} {y}')
