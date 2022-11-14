fname = importdata("data/fname.txt");
for k = 1:numel(fname)
	fprintf("%20s\t",fname{k})
	x = load(fname{k});
	tic
	y = fft(x);
	xx = ifft(x);
	t = toc;
    fprintf("%12d (ns)\n",round( 1e9 * t ))
end