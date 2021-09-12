from collections import deque
from functools import lru_cache


class Manager:

    def __init__(self, buckets_n):
        self.buckets_n = buckets_n
        self.mapping = tuple(deque() for _ in range(buckets_n))

    @lru_cache()
    def hash_it(self, text):
        p = 1000000007
        x = 263

        r = 0
        for i, s in enumerate(text):
            r += (ord(s) * x ** i)
        return r % p % self.buckets_n

    def add(self, value):
        hash_result = self.hash_it(value)
        if value not in self.mapping[hash_result]:
            self.mapping[hash_result].appendleft(value)

    def delete(self, value):
        hash_result = self.hash_it(value)
        try:
            index = self.mapping[hash_result].index(value)
            del self.mapping[hash_result][index]
        except ValueError:
            pass

    def find(self, value):
        hash_result = self.hash_it(value)
        try:
            self.mapping[hash_result].index(value)
            return 'yes'
        except ValueError:
            return 'no'

    def check(self, i):
        key = int(i)
        values = self.mapping[key]
        if values:
            return ' '.join(values)
        else:
            return ''

    def process_command(self, command):
        input_args = command.split()
        if input_args[0] == 'add':
            return self.add(*input_args[1:])
        elif input_args[0] == 'del':
            return self.delete(*input_args[1:])
        elif input_args[0] == 'find':
            return self.find(*input_args[1:])
        elif input_args[0] == 'check':
            return self.check(*input_args[1:])
        else:
            raise ValueError


def run():
    buckets_n = int(input())
    command_n = int(input())
    manager = Manager(buckets_n)
    for _ in range(command_n):
        output = manager.process_command(input())
        if output == '':
            yield None
        elif output:
            yield output


def run_test(commands):
    buckets_n = int(commands[0])
    command_n = int(commands[1])
    manager = Manager(buckets_n)
    for c in commands[2:]:
        output = manager.process_command(c)
        if output == '':
            yield None
        elif output:
            yield output


pass

if __name__ == '__main__':
    # case1 = [
    #     5,
    #     12,
    #     'add world',
    #     'add HellO',
    #     'check 4',
    #     'find World',
    #     'find world',
    #     'del world',
    #     'check 4',
    #     'del HellO',
    #     'add luck',
    #     'add GooD',
    #     'check 2',
    #     'del good',
    # ]
    # print(list(run_test(case1)))
    # print('###')
    # case2 = [
    #     4,
    #     8,
    #     'add test',
    #     'add test',
    #     'find test',
    #     'del test',
    #     'find test',
    #     'find Test',
    #     'add Test',
    #     'find Test',
    # ]
    # print(list(run_test(case2)))
    # print('###')
    # case3 = [
    #     3,
    #     12,
    #     'check 0',
    #     'find help',
    #     'add help',
    #     'add del',
    #     'add add',
    #     'find add',
    #     'find del',
    #     'del del',
    #     'find del',
    #     'check 0',
    #     'check 1',
    #     'check 2',
    # ]
    # print(list(run_test(case3)))

    for res in run():
        if res is None:
            print()
        else:
            print(res)
