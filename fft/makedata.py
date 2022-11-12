import numpy as np

# coefficients for sines and cosines
m = 10
a = -1 + 2*np.random.rand(m,2)

# sizes of arrays
nlist = np.loadtxt("nlist.txt", dtype = int)

# filenames
fname = [];

for n in nlist:

	# smooth data
	t = np.linspace(0,2*np.pi,n+1)
	t = t[0:n]
	x = np.zeros((n,))
	for k in range(m):
		x += a[k][0] * np.sin(k*t) + a[k][1] * np.cos(k*t)
	f = "data/smooth_%d.txt"%(n)
	np.savetxt(f,x)
	fname.append(f)

for n in nlist:

	# random data
	y = np.random.rand(n)
	f = "data/random_%d.txt"%(n)
	np.savetxt(f,y)
	fname.append(f)

# save filenames to file
f = open("data/fname.txt","w")
f.writelines("%s\n"%(s) for s in fname)
f.close()