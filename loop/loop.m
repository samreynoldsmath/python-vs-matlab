tic

n = 1e4;
A = zeros(n);

for i = 1:n
    for j = 1:n
        A(i,j) = i*j;
    end
end

toc 