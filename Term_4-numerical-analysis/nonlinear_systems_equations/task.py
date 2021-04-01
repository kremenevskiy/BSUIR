from sympy import symbols, log, sqrt, tan, atan
import numpy as np

k = 10
m = 0.1
a = 0.8

approx = (0.3, 0.7)
approx_2 = (0.05, -0.7)

# x, y = symbols('x y')
x = symbols('x:2')
y_1 = tan(x[0]*x[1] + m) - x[0]
y_2 = a*x[0]**2 + 2*x[1]**2 - 1


def get_system():
    return np.array([
        [
            y_1,
            y_2
        ],
        [
            tan(x[0]*x[1] + m),
            sqrt((1 - a*x[0]**2) / 2)
        ]
    ])


# def get_system_2():
#     return np.array([
#         [
#             y_1,
#             y_2
#         ],
#         [
#             (atan(x[0]) - 0.1) / x[1],
#             sqrt((1 - a*x[0]**2) / 2)
#         ]
#     ])

