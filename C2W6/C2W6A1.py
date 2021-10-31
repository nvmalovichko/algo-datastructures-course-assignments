import sys

sys.setrecursionlimit(10 ** 6)  # max depth of recursion


# Inorder (Left, Root, Right)
# Preorder (Root, Left, Right)
# Postorder (Left, Right, Root)


class Tree:
    root_index = None

    def __init__(self, n):
        self.n = n
        self.values = [None] * n
        self.lefts = [None] * n
        self.rights = [None] * n
        self.parents = [None] * n

    def update_node(self, i: int, value: str, left: int, right: int):
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
        result = []

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
            result.append(self.values[next_index])

            while True:
                # ----> right
                right_node_index = self.rights[next_index]
                if right_node_index is not None:
                    stack.append(right_node_index)
                    break
                if not stack:
                    break
                next_index = stack.pop()
                result.append(self.values[next_index])

        return result

    def preorder_traversal(self):
        stack = []
        result = []

        stack.append(self.root_index)
        result.append(self.values[self.root_index])
        while stack:
            # ----> left
            while stack:
                next_index = stack[-1]
                node_index = self.lefts[next_index]
                if node_index is not None:
                    stack.append(node_index)
                    result.append(self.values[node_index])
                else:
                    break

            # ----> back / pop stack
            next_index = stack.pop()

            while True:
                # ----> right
                right_node_index = self.rights[next_index]
                if right_node_index is not None:
                    stack.append(right_node_index)
                    result.append(self.values[right_node_index])
                    break
                if not stack:
                    break
                next_index = stack.pop()

        return result

    def postorder_traversal(self):
        stack_1 = []
        stack_2 = []

        stack_1.append(self.root_index)
        while stack_1:
            index = stack_1.pop()
            stack_2.append(index)
            if self.lefts[index] is not None:
                stack_1.append(self.lefts[index])
            if self.rights[index] is not None:
                stack_1.append(self.rights[index])
        return [self.values[x] for x in stack_2[::-1]]


def run():
    vertices_n = int(input())
    tree = Tree(vertices_n)
    for n, v in enumerate(range(vertices_n)):
        node_v, left_i, right_i = [int(x) for x in input().split()]
        tree.update_node(n, str(node_v), left_i, right_i)
    tree.find_root()

    print(' '.join(tree.inorder_traversal()))
    print(' '.join(tree.preorder_traversal()))
    print(' '.join(tree.postorder_traversal()))


def run_test(values):
    vertices = values[0]
    tree = Tree(vertices)
    for n, items in enumerate(values[1]):
        node_v, left_i, right_i = items
        tree.update_node(n, str(node_v), left_i, right_i)
    tree.find_root()

    print(' '.join(tree.inorder_traversal()))
    print(' '.join(tree.preorder_traversal()))
    print(' '.join(tree.postorder_traversal()))


if __name__ == '__main__':
    # case_1 = [
    #     10,
    #     [
    #         (0, 7, 2),
    #         (10, -1, -1),
    #         (20, -1, 6),
    #         (30, 8, 9),
    #         (40, 3, -1),
    #         (50, -1, -1),
    #         (60, 1, -1),
    #         (70, 5, 4),
    #         (80, -1, -1),
    #         (90, -1, -1),
    #     ]
    # ]
    # run_test(case_1)
    #
    # case_2 = [
    #     1,
    #     [
    #         (0, -1, -1),
    #     ]
    # ]
    # run_test(case_2)

    run()
