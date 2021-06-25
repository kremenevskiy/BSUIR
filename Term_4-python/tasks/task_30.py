# from collections import deque


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BSTIter:
    def __init__(self, root):
        self.prev_nodes = [(root, True)]  # node, is_left

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.prev_nodes) == 0:
            raise StopIteration
        cur_node, is_left = self.prev_nodes.pop()
        if is_left:
            while cur_node:
                self.prev_nodes.append((cur_node, False))
                cur_node = cur_node.left

            cur_node = self.prev_nodes.pop()[0]

        if cur_node.right:
            self.prev_nodes.append((cur_node.right, True))
        return cur_node


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

iter = BSTIter(tree_head)
for node in iter:
    print(node.value)
