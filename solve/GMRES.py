import numpy as np
from time import time
from scipy.sparse.linalg import gmres

def average_solve_time(A,b,num_trials):
    t = np.zeros((num_trials,))
    for k in range(num_trials):
        t[k] = -time()
        PA, Pb = Jacobi_precondition(A,b)
        x = gmres(PA,Pb)
        t[k] += time()
        return np.mean(t), np.std(t)

def Jacobi_precondition(A,b):
    P = np.diag(A)
    P = np.diag(1/P)
    return P@A, P@b

num_trials = 10
msg = "%8d\t%.4e\t%.4e\t%.4e"

print("%8s\t%10s\t%10s\t%10s"%("size","mean","stdev","cond"))

for j in range(4,13):
    n = int(2**j)
    A = np.random.rand(n,n)/np.sqrt(n) + 10*np.diag(np.random.rand(n))
    b = np.random.rand(n)
    c = np.linalg.cond(A)
    mean_time, std_time = average_solve_time(A,b,num_trials)
    print(msg%(n,mean_time,std_time,c))
