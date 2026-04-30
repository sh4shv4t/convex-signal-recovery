function [x_opt, obj_val, status] = solve_case2(A, b_bar)
%SOLVE_CASE2 Solve case 2: minimize sum(x) subject to A*x >= b_bar.

    n = size(A, 2);
    cvx_begin quiet
        variable x(n)
        minimize( sum(x) )
        subject to
            A * x >= b_bar;
    cvx_end

    x_opt = x;
    obj_val = cvx_optval;
    status = cvx_status;
end
