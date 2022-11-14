import numpy as np
from time import time

t = -time()

n = int(1e4)
x = np.linspace(1,n,n)
A = np.outer(x,x)

t += time()

print(t)