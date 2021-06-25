class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def BSTGen(tree_head: Node):
    def rec(node):
        if node is None:
            return

        left_l = list(rec(node.left))
        for left_el in left_l:
            yield left_el

        yield node

        right_ls = list(rec(node.right))
        for right_el in right_ls:
            yield right_el

    base_l = list(rec(tree_head))
    for el in base_l:
        yield el


data = [5, 2, 8, -3, 2, 0, 4]

tree_head = Node(5)
nodes = [Node(e) for e in data]
tree_head.left = nodes[0]
tree_head.right = nodes[1]
nodes[0].left = nodes[2]
nodes[0].right = nodes[4]
nodes[2].left = nodes[3]
nodes[3].right = nodes[6]
nodes[1].right = nodes[5]

for node in BSTGen(tree_head):
    print(node.value)


def bst_generator(head):
    if head.left is not None:
        yield from bst_generator(head.left)
    yield head
    if head.right is not None:
        yield from bst_generator(head.right)


print()

for node in bst_generator(tree_head):
    print(node.value)
