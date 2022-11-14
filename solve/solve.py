import numpy as np
from time import time

def average_solve_time(A,b,num_trials):
    t = np.zeros((num_trials,))
    for k in range(num_trials):
        t[k] = -time()
        x = np.linalg.solve(A,b)
        t[k] += time()
        return np.mean(t), np.std(t)

num_trials = 10
msg = "%8d\t%.4e\t%.4e"

print("%8s\t%10s\t%10s"%("size","mean","stdev"))

for j in range(4,13):
    n = int(2**j)
    A = np.random.rand(n,n)
    b = np.random.rand(n)
    mean_time, std_time = average_solve_time(A,b,num_trials)
    print(msg%(n,mean_time,std_time))
