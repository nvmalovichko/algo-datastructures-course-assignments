# /usr/bin/python3

MEMO = dict()

OPERATIONS = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x * 3,
]


def get_count(number):
    if number == 1:
        return [1], 0

    MEMO[1] = (1, 0)  # from number, counter
    for i in range(1, number + 1):
        from_number, counter = MEMO[i]
        for op in OPERATIONS:
            next_value = op(i)
            if next_value > number:
                continue

            if MEMO.get(next_value, None) is None:
                MEMO[next_value] = (i, counter + 1)
            else:
                next_from_number, next_counter = MEMO[next_value]
                if next_counter > counter + 1:
                    MEMO[next_value] = (i, counter + 1)

    next_v, counter = MEMO[number]
    values = [number]
    c_ = 1
    while c_ != 0:
        values.append(next_v)
        next_v, c_ = MEMO[next_v]

    return values[::-1], counter


if __name__ == '__main__':
    number = int(input())
    MEMO = {i: None for i in range(1, number + 1)}
    numbers, counter = get_count(number)

    print(counter)
    print(' '.join(str(x) for x in numbers))
