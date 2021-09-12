# /usr/bin/python3

MEMO = dict()

OPERATIONS = [
    lambda x: x + 1,
    lambda x: x + 3,
    lambda x: x + 4,
]


def get_count(number):
    if number == 1:
        return 1

    MEMO[0] = 0  # counter
    for i in range(number + 1):
        counter = MEMO[i]
        for op in OPERATIONS:
            next_value = op(i)
            if next_value > number:
                continue

            if MEMO.get(next_value, None) is None:
                MEMO[next_value] = counter + 1
            else:
                next_counter = MEMO[next_value]
                if next_counter > counter + 1:
                    MEMO[next_value] = counter + 1
    return MEMO[number]


if __name__ == '__main__':
    number = int(input())
    MEMO = {i: None for i in range(number + 1)}
    print(get_count(number))

