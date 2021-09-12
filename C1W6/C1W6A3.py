import math
import re

CALC = {
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}


def minmax(i, j, matrix_m, matrix_M, symbols):
    mini, maxi = math.inf, -math.inf
    for k in range(i, j):
        symb = symbols[k]

        # m - m
        a = CALC[symb](matrix_m[i][k], matrix_m[k + 1][j])
        # m - M
        b = CALC[symb](matrix_m[i][k], matrix_M[k + 1][j])
        # M - m
        c = CALC[symb](matrix_M[i][k], matrix_m[k + 1][j])
        # M - M
        d = CALC[symb](matrix_M[i][k], matrix_M[k + 1][j])

        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return mini, maxi


def run_it(text):
    numbers = [int(x) for x in re.split(r'[+*-]', text)]
    symbols = [x for x in re.split(r'\d+', text) if x]
    numbers_len = len(numbers)
    matrix_m = [[None for i in range(numbers_len)] for j in range(numbers_len)]
    matrix_M = [[None for i in range(numbers_len)] for j in range(numbers_len)]

    for i in range(numbers_len):
        matrix_m[i][i] = numbers[i]
        matrix_M[i][i] = numbers[i]

    # print(numbers, symbols, matrix_m, matrix_M)

    for n in range(1, numbers_len):
        for row in range(numbers_len - n):
            col = row + n
            row = row
            min_v, max_v = minmax(row, col, matrix_m, matrix_M, symbols)
            matrix_m[row][col] = min_v
            matrix_M[row][col] = max_v
            # print(matrix_m, '\n', matrix_M, '\n###')
    return matrix_M[0][numbers_len - 1]


if __name__ == '__main__':
    # assert run_it('1-2*3+4') == 1
    # assert run_it('1+5') == 6
    # assert run_it('5-8+7*4-8+9') == 200

    input_str = input()

    print(run_it(input_str))
