import numpy as np

v = np.array([3, 4])

print("Vector:", v)
print("Norm:", np.linalg.norm(v))
print("Unit vector:", v / np.linalg.norm(v))

import numpy as np

a = np.array([2, 1])
b = np.array([3, 2])

print("a + b =", a + b)
print("a - b =", a - b)
print("2a =", 2 * a)
print("-a =", -a)
print("Unit vector of a =", a / np.linalg.norm(a))