import numpy as np
from time import time

t = -time()

n = int(1e4)
A = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        A[i][j] = i*j

t += time()

print(t)