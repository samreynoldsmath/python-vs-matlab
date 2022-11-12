fname = load("data/fname.txt");
for s = fname
	disp(s)
	x = load(s);
	tic
	y = fft(x);
	xx = ifft(x);
	toc
end