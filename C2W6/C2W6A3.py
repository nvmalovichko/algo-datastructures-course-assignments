class Tree:
    root_index = None

    def __init__(self, n):
        self.n = n
        self.values = [None] * n
        self.lefts = [None] * n
        self.rights = [None] * n
        self.parents = [None] * n

    def update_node(self, i: int, value: int, left: int, right: int):
        self.values[i] = value

        if left != -1:
            self.lefts[i] = left
            self.parents[left] = i

        if right != -1:
            self.rights[i] = right
            self.parents[right] = i

    def find_root(self):
        for i, p in enumerate(self.parents):
            if p is None:
                self.root_index = i
                break

    def inorder_traversal(self):
        stack = []

        stack.append(self.root_index)
        while stack:
            # ----> left
            while stack:
                next_index = stack[-1]
                node_index = self.lefts[next_index]
                if node_index is not None:
                    stack.append(node_index)
                else:
                    break

            # ----> back / pop stack
            next_index = stack.pop()
            yield next_index

            while True:
                # ----> right
                right_node_index = self.rights[next_index]
                if right_node_index is not None:
                    stack.append(right_node_index)
                    break
                if not stack:
                    break
                next_index = stack.pop()
                yield next_index

    def is_valid(self):
        indexes = []
        for index in self.inorder_traversal():
            indexes.append(index)
            if len(indexes) > 1:
                index_left = indexes[-2]
                index_right = indexes[-1]
                if self.lefts[index_right] == index_left and self.values[index_right] == self.values[index_left]:
                    return False
                elif self.values[index_right] < self.values[index_left]:
                    return False
        return True


def run():
    result = 'CORRECT'
    vertices_n = int(input())
    if vertices_n > 1:
        tree = Tree(vertices_n)
        for n, v in enumerate(range(vertices_n)):
            node_v, left_i, right_i = [int(x) for x in input().split()]
            tree.update_node(n, node_v, left_i, right_i)
        tree.find_root()
        result = 'CORRECT' if tree.is_valid() else 'INCORRECT'
    print(result)


def run_test(values):
    result = 'CORRECT'
    vertices_n = values[0]
    if vertices_n > 1:
        tree = Tree(vertices_n)
        for n, items in enumerate(values[1]):
            node_v, left_i, right_i = items
            tree.update_node(n, node_v, left_i, right_i)
        tree.find_root()
        result = 'CORRECT' if tree.is_valid() else 'INCORRECT'

    return result


if __name__ == '__main__':
    # case_1 = [
    #     3,
    #     [
    #         (-8, -1, 1),
    #         (-7, -1, 2),
    #         (-6, -1, -1),
    #     ],
    #     'CORRECT'
    # ]
    # case_2 = [
    #     0,
    #     [
    #     ],
    #     'CORRECT'
    # ]
    # case_3 = [
    #     1,
    #     [
    #         (1, -1, -1),
    #     ],
    #     'CORRECT'
    # ]
    # case_4 = [
    #     3,
    #     [
    #         (2, 1, 2),
    #         (1, -1, -1),
    #         (3, -1, -1),
    #     ],
    #     'CORRECT'
    #
    # ]
    # case_5 = [
    #     3,
    #     [
    #         (2, 1, 2),
    #         (2, -1, -1),
    #         (3, -1, -1),
    #     ],
    #     'INCORRECT'
    # ]
    # case_6 = [
    #     3,
    #     [
    #         (2, 1, 2),
    #         (1, -1, -1),
    #         (2, -1, -1),
    #     ],
    #     'CORRECT'
    # ]
    # for case_x in [case_1, case_2, case_3, case_4, case_5, case_6]:
    #     *params, answer = case_x
    #     assert run_test(params) == answer, case_x

    run()
