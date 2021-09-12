# /usr/bin/python3

MATRIX = []


def get_count(string_vert, string_hor):
    for col in range(len(string_vert) + 1):
        for row in range(len(string_hor) + 1):
            if MATRIX[col][row] is None:
                if col == 0:
                    MATRIX[col][row] = MATRIX[col][row - 1] + 1
                elif row == 0:
                    MATRIX[col][row] = MATRIX[col - 1][row] + 1
                else:
                    if string_vert[col - 1] == string_hor[row - 1]:
                        MATRIX[col][row] = min(MATRIX[col][row - 1] + 1,
                                               MATRIX[col - 1][row] + 1,
                                               MATRIX[col - 1][row - 1])
                    else:
                        MATRIX[col][row] = min(MATRIX[col][row - 1] + 1,
                                               MATRIX[col - 1][row] + 1,
                                               MATRIX[col - 1][row - 1] + 1)
    return MATRIX[len(string_vert)][len(string_hor)]


if __name__ == '__main__':
    string_vert = input()
    string_hor = input()

    MATRIX.append([0] + [None] * len(string_hor))
    for i in range(len(string_vert)):
        MATRIX.append([None] * (len(string_hor) + 1))

    print(get_count(string_vert, string_hor))
