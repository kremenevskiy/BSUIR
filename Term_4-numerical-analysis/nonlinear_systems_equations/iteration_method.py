from sympy import symbols, solve, exp, log, E
import numpy as np
from scipy.optimize import fsolve
from staff_matrix import get_jacobi, roots_to_dict, check_norm


def iteration_solve(system_equations: np.array, approx, tol=0.0001):
    n = system_equations.shape[0]
    x = symbols(f'x:{n}')

    fi_equations = system_equations[1]

    prev_roots = np.zeros(shape=(n, ))
    curr_roots = list(approx)

    errors = np.zeros(shape=(n, ))
    error = tol * 10000

    J = get_jacobi(system_equations[0])
    jacabi_values = np.zeros(shape=(n, n))

    roots_d = roots_to_dict(curr_roots, x)

    for i in range(n):
        for j in range(n):
            jacabi_values[i, j] = J[i, j].subs(roots_d)

    iteration = 0
    while error > tol:
        prev_roots = curr_roots.copy()
        roots_d = roots_to_dict(curr_roots, x)
        for i in range(n):
            try:
                curr_roots[i] = float(fi_equations[i].subs(roots_d))
            except TypeError:
                print("some complex numbers")

            errors[i] = abs(prev_roots[i] - curr_roots[i])
            roots_d = roots_to_dict(curr_roots, x)

        error = np.amax(errors)
        iteration += 1

    return curr_roots, iteration

