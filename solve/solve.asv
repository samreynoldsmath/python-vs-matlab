num_trials = 10;
msg = "%8d\t%.4e\t%.4e\n";

fprintf("%8s\t%10s\t%10s\n","size","mean","stdev");

for j = 4:12
    n = 2^j;
    A = rand(n);
    b = rand(n,1);
    [mean_time,std_time] = average_solve_time(A,b,num_trials);
    fprintf(msg,n,mean_time,std_time);
end

function [mean_time,std_time] = average_solve_time(A,b,num_trials)
    t = zeros(1,num_trials);
    for k = 1:num_trials
        tic
        x = A\b;
        t(k) = toc;
    end
    mean_time = mean(t);
    std_time = std(t);
end