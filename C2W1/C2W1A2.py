class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = list()


def get_height(params, n_nodes):
    root_node = None
    nodes = [Node(i) for i in range(n_nodes)]
    for n, p in enumerate(params):
        node = nodes[n]
        if p != -1:
            parent_node = nodes[p]
            node.parent = parent_node
            parent_node.children.append(node)
        else:
            root_node = nodes[n]

    if root_node:
        max_height = 0

        stack = [root_node]
        while stack:
            children = list()
            while stack:
                node = stack.pop()
                children.extend(node.children)
            stack.extend(children)
            max_height += 1
        return max_height
    else:
        raise ValueError


if __name__ == '__main__':
    # assert get_height([4, -1, 4, 1, 1], 5) == 3
    # assert get_height([-1, 0, 4, 0, 3], 5) == 4

    n_nodes = int(input())
    params = [int(v) for v in input().split()]
    print(get_height(params, n_nodes))
