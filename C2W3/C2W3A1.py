class Manager:

    def __init__(self):
        self.mapping = dict()

    def add(self, number, name):
        self.mapping[int(number)] = name

    def delete(self, number):
        self.mapping[int(number)] = None

    def find(self, number):
        return self.mapping.get(int(number), None) or 'not found'

    def process_command(self, command):
        input_args = command.split()
        if input_args[0] == 'add':
            return self.add(*input_args[1:])
        elif input_args[0] == 'del':
            return self.delete(*input_args[1:])
        elif input_args[0] == 'find':
            return self.find(*input_args[1:])
        else:
            raise ValueError


def run():
    manager = Manager()

    command_n = int(input())
    for _ in range(command_n):
        output = manager.process_command(input())
        if output:
            print(output)


def run_test(commands):
    manager = Manager()
    command_n = int(commands[0])
    for c in commands[1:]:
        output = manager.process_command(c)
        if output:
            print(output)


pass

if __name__ == '__main__':
    # case1 = [
    #     '12',
    #     'add 911 police',
    #     'add 76213 Mom',
    #     'add 17239 Bob',
    #     'find 76213',
    #     'find 910',
    #     'find 911',
    #     'del 910',
    #     'del 911',
    #     'find 911',
    #     'find 76213',
    #     'add 76213 daddy',
    #     'find 76213',
    # ]
    # case2 = [
    #     8,
    #     'find 3839442',
    #     'add 123456 me',
    #     'add 0 granny',
    #     'find 0',
    #     'find 123456',
    #     'del 0',
    #     'del 0',
    #     'find 0',
    # ]
    # run_test(case1)
    # print('###')
    # run_test(case2)

    run()
