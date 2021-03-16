import numpy as np
from extra_tools import *

from gauss_standart import gauss_solve
from gauss_column_selection import gauss_column_selection
from gauss_full_matrix_selection import gauss_main_selection

import tests
import task

A = task.A
b = task.b

print('Исходная система уравнений:')
print_equation(A, b)

print(f'Решение методом Гаусса без модификаций :)')
print_x(gauss_solve(A, b, 0))

print(f'\nРешение методом Гаусса с выбором главного элемента по столбцу :)')
print_x(gauss_column_selection(A, b, 0))

print(f'\nРешение методом Гаусса с выбором главного элемента по всей матрице :)')
print_x(gauss_main_selection(A, b, 0))
