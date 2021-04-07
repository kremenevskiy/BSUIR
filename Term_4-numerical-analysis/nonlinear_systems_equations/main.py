import numpy as np
from iteration_method import *
from sympy import *
import tests
import task
from newton_method import *


def print_list(ls, ):
    output = ["%.4f" % el for el in ls]
    return output


def main():
    pass


# if __name__ == '__main__':
#     main()


system = task.get_system()
approx = task.approx


print(f"\t\tНачальное приближение: {approx}")
iteration_ans = iteration_solve(system, approx, verbose=1)
print("\t\t*** Метод простой итерации: ***")
print(f"Корни уравнения: {print_list(iteration_ans[0])}")
print(f"Количество итераций: {iteration_ans[1]}")

for i in range(2):
    print('-' * 20)


print(f"\t\tНачальное приближение: {approx}")
newton_ans = newton_solve(system[0], approx)
print("\t\t*** Метод Ньютона: ***")
print(f"Корни уравнения: {print_list(newton_ans[0])}")
print(f"Количество итераций: {newton_ans[1]}")
