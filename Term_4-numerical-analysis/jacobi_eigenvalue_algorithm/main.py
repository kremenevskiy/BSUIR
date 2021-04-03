import numpy as np
from jacobi_eigen_method import find_eigen
from staff import print_array, separator
import task
import tests


E = task.E
A = task.A


eig_val, eig_vec, steps = find_eigen(A, E, 1)


print_array(A, 'Default Matrix:')
print_array(eig_val, '\nMatrix of Eigenvalues:')
print_array(eig_val @ np.ones(shape=(eig_val.shape[0], )), 'Eigenvalues:')
print_array(eig_vec, 'Eigenvectors:')


print("\nVerification:")

w, v = np.linalg.eig(A)
print_array(w, 'Eigenvalues (numpy):')
print_array(v, 'Eigenvectors (numpy):')















