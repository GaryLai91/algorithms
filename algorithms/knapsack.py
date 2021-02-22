import numpy as np
from collections import namedtuple, deque

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])


class Node:
    def __init__(self, value, weight, estimate, level, taken):
        self.value = value
        self.weight = weight
        self.estimate = estimate
        self.level = level
        self.taken = taken


def get_input(filename):
    items = []
    with open(filename, 'r') as f:
        line = f.readline().strip().split(" ")
        capacity, n_items = int(line[0]), int(line[1])
        for n in range(n_items):
            line = f.readline().strip().split(" ")
            value, weight = int(line[0]), int(line[1])
            density = value / weight
            items.append(
                Item(index=n, value=value, weight=weight, density=density))
    items = sorted(items, key=lambda x: x.density, reverse=True)
    return items, capacity


def recursion(items, capacity):
    items = tuple(items)
    value = 0
    weight = 0
    taken = [0] * len(items)
    table = np.array([[0] * (len(items) + 1) for i in range(capacity + 1)])

    def recurse(k, j):
        if (j == 0):
            return 0
        elif (items[j - 1].weight <= k):
            max_ = max(
                table[k][j - 1],
                items[j - 1].value + table[k - items[j - 1].weight][j - 1])
            return max_
        else:
            return table[k][j - 1]

    for j in range(1, len(items) + 1):
        for k in range(1, capacity + 1):
            table[k][j] = recurse(k, j)

    row, col = capacity, len(items)
    while capacity >= 0 and row > 0 and col > 0:
        if table[row][col] != table[row][col - 1]:
            capacity -= items[col - 1].weight
            row -= items[col - 1].weight
            col -= 1
            taken[items[col].index] = 1
            value += items[col].value
        else:
            col -= 1
    return value, taken


def bound(node, capacity, items):
    if node.weight <= 0:
        return 0
    value_bound = node.value
    j = node.level
    total_weight = node.weight
    while (j < len(items)) and (total_weight - items[j].weight >= 0):
        total_weight -= items[j].weight
        value_bound += items[j].value
        j += 1
    if (j < len(items)):
        value_bound += (total_weight) * items[j].value / items[j].weight
    return value_bound


def branch(items, capacity):
    value = 0
    taken = [0] * len(items)
    root = Node(0, capacity, 0, 0, taken)
    root.estimate = bound(root, capacity, items)
    q = deque()
    q.append(root)
    while len(q) > 0:
        u = q.pop()
        if u.level == len(items) or u.estimate <= value:
            continue

        #left means take item
        left_node = Node(0, 0, 0, 0, [])
        left_node.value = u.value + items[u.level].value
        left_node.weight = u.weight - items[u.level].weight
        left_node.level = u.level + 1
        left_node.estimate = bound(left_node, left_node.weight, items)
        left_node.taken = u.taken[:]
        left_node.taken[items[u.level].index] = 1

        # right means don't take item
        right_node = Node(0, 0, 0, 0, [])
        right_node.value = u.value
        right_node.weight = u.weight
        right_node.level = u.level + 1
        right_node.estimate = bound(right_node, right_node.weight, items)
        right_node.taken = u.taken[:]
        right_node.taken[items[u.level].index] = 0

        if right_node.weight >= 0:
            q.append(right_node)
            if right_node.value > value:
                value = right_node.value
                taken = right_node.taken

        if left_node.weight >= 0:
            q.append(left_node)
            if left_node.value > value:
                value = left_node.value
                taken = left_node.taken

    return value, taken


if __name__ == "__main__":
    items, capacity = get_input("test.txt")
    value, taken = recursion(items, capacity)
    print(value)