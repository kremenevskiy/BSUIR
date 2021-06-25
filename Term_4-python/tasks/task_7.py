import random

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def travesse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def sort(self):
        all_nodes = []
        current = self.head
        while current is not None:
            all_nodes.append(current.value)
            current = current.next

        sorted_values = sorted(all_nodes)

        sorted_list = LinkedList()
        for i in sorted_values:
            node = Node(i)
            sorted_list.add_new(node)

        return sorted_list



    def add_new(self, node=None):

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node


def delete_duplicates(head: Node) -> Node:
    current = head
    if head is None:
        return Node()

    nextnode = head.next

    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
            continue

        current = current.next
    return head


linked = LinkedList()
for i in range(100):
    temp_node = Node(random.randint(0, 10))
    linked.add_new(temp_node)


sorted_list = linked.sort()
sorted_list.travesse()

sorted_head = sorted_list.head
new_head = delete_duplicates(sorted_head)

new_list = LinkedList(new_head)
new_list.travesse()

