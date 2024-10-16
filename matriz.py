import numpy as np
A = np.random.randint(11, size=(4, 3))
print(f"Matriz: \n{A}\n")
nueva_matriz = np.delete(A, 2, axis=1)

print(f"Nueva matriz:\n{nueva_matriz}\n")
