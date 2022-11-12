import numpy as np
import time

# open data
f = open("data/fname.txt","r")
fname = f.readlines()
f.close()

for s in fname:

	s = s.replace("\n","")
	x = np.loadtxt(s)
	t = - time.time_ns()

	# the test
	y = np.fft.fft(x)
	xx = np.fft.ifft(y)

	t += time.time_ns()
	print("%20s\t%d"%(s,t))