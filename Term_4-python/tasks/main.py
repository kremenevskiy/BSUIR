# import task_1
# import task_2
# import task_3

import math



import random


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next


def partition(head, x):
    less, big, less_head, big_head = None, None, None, None
    current = head
    while current is not None:
        if current.value < x:
            if less_head is None:
                less_head = current
                less = current
            else:
                less.next = current
                less = less.next
        else:
            if big_head is None:
                big_head = current
                big = current
            else:
                big.next = current
                big = big.next
        current = current.next
    if less_head is None:
        return big_head
    if big_head is None:
        return less_head
    less.next = big_head
    big.next = None
    return less_head


# x = 5
arr = [int(item) for item in input("arr: ").split()]
x = int(input("x: "))

head = Node(arr[0])
prev = head
for i in range(1, len(arr)):
    current = Node(arr[i])
    prev.next = current
    prev = current

# head = Node()
# prev = head
# for i in range(15):
#     value = random.randint(0, 10)
#     current = Node(value)
#     prev.next = current
#     prev = current

print_list(head)
print()
head = partition(head, x)
print_list(head)