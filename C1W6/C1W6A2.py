import copy

MEMO = list()


def run_it(values, items_n):
    def calc(items, volume, items_n):
        matrix = [[(0, tuple()) for i in range(volume + 1)] for j in range(items_n + 1)]

        for numb in range(items_n + 1):
            if numb == 0:
                continue

            item_i = items[numb - 1]
            for vol in range(volume + 1):
                if vol == 0:
                    continue

                matrix[numb][vol] = matrix[numb - 1][vol]
                if item_i <= vol:
                    value_n = matrix[numb - 1][vol - item_i][0] + item_i
                    value_tuple = matrix[numb - 1][vol - item_i][1] + (item_i,)
                    value = (value_n, value_tuple)
                    matrix[numb][vol] = max(matrix[numb][vol], value, key=lambda x: x[0])

            if matrix[numb][volume][0] == volume:
                return matrix[numb][volume]

        return matrix[items_n][volume]

    ###
    values = sorted(values)

    sum_items = sum(values)
    if len(values) < 3 or sum_items % 3:
        return 0

    volume = int(sum_items / 3)

    # # --- optimization 1
    # for m in (10000, 1000, 100, 10):
    #     if not volume % m and all(not v % m for v in values):
    #         values = [int(v / m) for v in values]
    #         volume = int(volume / m)
    #         break
    #
    # # --
    #
    # # --- optimization 2
    # sum_items = sum(values)
    # volume = sum_items if volume - sum_items > 0 else volume
    # # --

    values_ = copy.copy(values)
    for _ in range(2):
        distinct_values = sorted(set(values_))
        value, options = calc(distinct_values, volume, len(distinct_values))
        if value != volume:
            return 0
        for i in options:
            values_.remove(i)
    return 1


if __name__ == '__main__':
    # assert run_it([3, 3, 3, 1, 1, 1], 6) == 1
    # assert run_it([40], 1) == 0
    # assert run_it([3, 5, 1], 3) == 0
    # assert run_it([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 11) == 1
    # assert run_it([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 13) == 1
    # assert run_it([1, 2, 2, 3, 4, 5, 10], 7) == 0
    # assert run_it([1, 1, 1, 2, 2, 2], 6) == 1
    # assert run_it([0, 1, 2, 3, 3, 3, 3, 3, 3, 3], 10) == 0
    # assert run_it([0, 0, 0, 0, 0, 0, 1], 7) == 0

    items_n = int(input())
    items = [int(x) for x in input().split()]

    print(run_it(items, items_n))
