class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


arr = [2, 1]

head = Node(arr[0])
prev = head
for i in range(1, len(arr)):
    current = Node(i)
    prev.next = current
    prev = current


def traverse(head: Node):
    if head is Node:
        return

    while head is not None:
        print(head.value, end=' ')
        head = head.next


traverse(head)
print()


def partition(head: Node, x: int) -> Node:
    left_head, left, right_head, right = None, None, None, None
    current = head
    while current is not None:
        if current.value < x:
            if left_head is None:
                left_head = current
                left = current
            else:
                left.next = current
                left = left.next
        else:
            if right_head is None:
                right_head = current
                right = current
            else:
                right.next = current
                right = right.next
        current = current.next

    if left_head is None:
        return right_head
    if right_head is None:
        return left_head

    left.next = right_head
    right.next = None
    return left_head


traverse(partition(head, 2))