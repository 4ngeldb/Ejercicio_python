import numpy as np
A = np.random.randint(20, size=(3, 3))
B = np.random.randint(20, size=(3, 3))


print(f"Matriz A:\n {A} \n")
print(f"Matriz B:\n {B}\n")
C = np.matmul(A, B)
print(f"Matriz resul:\n {C}")
