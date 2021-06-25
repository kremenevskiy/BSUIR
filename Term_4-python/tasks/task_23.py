import math


class Vector:
    def __init__(self, *args, values=None):
        self.values = []

        if values is not None:
            self.values = values
        else:
            for i in args:
                self.values.append(i)

        self.size = len(self.values)

    def get_length(self):
        length = 0
        for i in self.values:
            length += i ** 2
        length = math.sqrt(length)
        return length

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("vector must be same size")
        values = []
        for i in range(self.size):
            values.append(self.values[i] + other.values[i])
        return Vector(values=values)

    def __iadd__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("vector must be same size")

        for i in range(self.size):
            self.values[i] += other.values[i]
        return self

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("vector must be same size")
        values = []
        for i in range(self.size):
            values.append(self.values[i] - other.values[i])
        return Vector(values=values)

    def __isub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("vector must be same size")

        for i in range(self.size):
            self.values[i] -= other.values[i]
        return self

    def __eq__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("vector must be same size")

        # for i in range(self.size):
        #     if self.values[i] == other.values[i]:
        #         continue
        #     else:
        #         return False
        # return True

        return self.get_length() == other.get_length()

    def __str__(self):

        string_ints = [str(i) for i in self.values]
        string = f'\tVector of size: {self.size}\nValues: '
        string += ", ".join(string_ints)
        return string


v1 = Vector(1, 2, 3, 4, 5, 6)
v2 = Vector(1, 2, 3, 4, 5, 6)

print(v1 + v2)
print(f'Equal: {v1 == v2}')


