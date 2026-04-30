function [x_opt, obj_val, status] = solve_case3(A, b_bar)
%SOLVE_CASE3 Solve case 3: minimize sum(x) subject to A*x >= b_bar and -1 <= x <= 1.

    n = size(A, 2);
    cvx_begin quiet
        variable x(n)
        minimize( sum(x) )
        subject to
            A * x >= b_bar;
            x >= -1;
            x <= 1;
    cvx_end

    x_opt = x;
    obj_val = cvx_optval;
    status = cvx_status;
end
