def check_str(value):
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    brackets_open = brackets.values()
    brackets_close = brackets.keys()
    stack = list()
    for i, char in enumerate(value, 1):
        if char in brackets_open:
            stack.append((char, i))
        elif char in brackets_close:
            try:
                open_char = brackets[char]
                last_bracket, pos = stack.pop()
                if last_bracket != open_char:
                    return i
            except IndexError:
                return i

    if not stack:
        return 'Success'
    else:
        last_bracket, pos = stack[0]
        return pos


if __name__ == '__main__':
    # assert check_str(']()') == 1
    # assert check_str('([])(') == 5
    # assert check_str('{([()])}') == 'Success'
    # assert check_str('foo(bar[i);') == 10
    # assert check_str('foo(bar);') == 'Success'
    # assert check_str('[]') == 'Success'
    # assert check_str('{}[]') == 'Success'
    # assert check_str('[()]') == 'Success'
    # assert check_str('(())') == 'Success'
    # assert check_str('{[]}()') == 'Success'
    # assert check_str('{') == 1
    # assert check_str('[](()') == 3
    # assert check_str('[]((){{}') == 3
    # assert check_str('{[}') == 3

    value = input()
    print(check_str(value))
