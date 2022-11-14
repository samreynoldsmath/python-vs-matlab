num_trials = 10;
msg = "%8d\t%.4e\t%.4e\t%.4e\n";

fprintf("%8s\t%10s\t%10s\t%10s\n","size","mean","stdev","cond");

for j = 4:12
    n = 2^j;
    A = rand(n)/sqrt(n) + 10*diag(rand(n,1));
    b = rand(n,1);
    c = cond(A);
    [mean_time,std_time] = average_solve_time(A,b,num_trials);
    fprintf(msg,n,mean_time,std_time,c);
end

function [PA,Pb] = Jacobi_precondition(A,b)
    P = diag(A);
    P = diag(1./P);
    PA = P*A;
    Pb = P*b;
end

function [mean_time,std_time] = average_solve_time(A,b,num_trials)
    t = zeros(1,num_trials);
    for k = 1:num_trials
        tic
        [PA,Pb] = Jacobi_precondition(A,b);
        [x,flag] = gmres(PA,Pb);
        t(k) = toc;
    end
    mean_time = mean(t);
    std_time = std(t);
end