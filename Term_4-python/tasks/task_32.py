class FlattenIterator:
    def __iter__(self):
        return self

    def __init__(self, lst):
        self.stack = [[lst, 0]]

    def __next__(self):
        while True:
            lst = self.stack[-1][0]
            index = self.stack[-1][1]
            if index < len(lst):
                self.stack[-1][1] += 1
                if type(lst[index]) != list:
                    return lst[index]
                else:
                    self.stack.append([lst[index], 0])
            else:
                self.stack.pop()
                if len(self.stack) == 0:
                    raise StopIteration


# lst = [[1, 1], [2], [1, 1]]
lst = [[1, [1, 3]], 2, [1, 4, [6]]]
for i in FlattenIterator(lst):
    print(i, end=" ")