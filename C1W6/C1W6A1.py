def run_it(values, volume, items_n):
    def calc(items, volume, items_n):
        matrix = [[0 for i in range(volume + 1)] for j in range(items_n + 1)]

        for numb in range(items_n + 1):
            if numb == 0:
                continue

            item_i = items[numb - 1]
            for vol in range(volume + 1):
                if vol == 0:
                    continue
                matrix[numb][vol] = matrix[numb - 1][vol]
                if item_i <= vol:
                    value = matrix[numb - 1][vol - item_i] + item_i
                    matrix[numb][vol] = max(matrix[numb][vol], value)

        return matrix[items_n][volume]

    ###
    values = tuple(sorted(values))

    # --- optimization 1
    multi = 1
    for m in (10000, 1000, 100, 10):
        if not volume % m and all(not v % m for v in values):
            values = tuple(int(v / m) for v in values)
            volume = int(volume / m)
            multi = m
            break

    # --

    # --- optimization 2
    sum_items = sum(values)
    volume = sum_items if volume - sum_items > 0 else volume
    # --

    result = calc(values, volume, items_n)
    return result * multi


if __name__ == '__main__':
    # assert run_it((1, 3, 5), 10, 3) == 9
    # assert run_it((1, 4, 8), 10, 3) == 9
    # assert run_it((100, 22, 44), 10, 3) == 0
    # assert run_it((100,), 1000, 1) == 100
    # assert run_it((5, 7, 12, 18), 20, 4) == 19
    # assert run_it((1, 2, 3, 3, 5, 3, 5, 4), 10, 8) == 10
    # assert run_it((100,) * 300, 10000, 300) == 10000

    volume, items_n = [int(x) for x in input().split()]
    values = tuple(int(x) for x in input().split())

    print(run_it(values, volume, items_n))
