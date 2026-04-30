% main.m - Entry point for convex signal recovery experiments.
% Runs all three constraint cases and produces plots and summaries.

rng(42); % reproducibility

[A, x_true, b_bar, y_bar] = generate_data();

% Solve all three cases
[x1, obj1, status1] = solve_case1(A, b_bar);
[x2, obj2, status2] = solve_case2(A, b_bar);
[x3, obj3, status3] = solve_case3(A, b_bar);

statuses = {status1, status2, status3};
[obj_vals, norms] = summarize_results({x1, x2, x3}, statuses, [obj1, obj2, obj3]);

% Print results table
fprintf('\n%-6s | %-20s | %-14s | %-12s\n', 'Case', 'CVX Status', 'Objective', '||x||_2');
fprintf('%s\n', repmat('-', 1, 62));
for k = 1:3
    fprintf('%-6s | %-20s | %-14.6g | %-12.6g\n', ...
        sprintf('Case %d', k), statuses{k}, obj_vals(k), norms(k));
end

% Plot results and save figures
plot_results(x1, x2, x3, obj_vals, statuses);

% Local helper functions
function [obj_vals, norms] = summarize_results(x_cells, statuses, raw_obj)
%SUMMARIZE_RESULTS Normalize outputs and warn on infeasible/unbounded cases.

    obj_vals = raw_obj;
    norms = nan(1, numel(x_cells));
    for i = 1:numel(x_cells)
        if is_solved(statuses{i})
            norms(i) = norm(x_cells{i});
        else
            obj_vals(i) = nan;
            norms(i) = nan;
            warning('Case %d not solved: %s', i, statuses{i});
        end
    end
end

function tf = is_solved(status)
%IS_SOLVED Return true if the CVX status indicates a solved problem.

    tf = contains(status, 'Solved', 'IgnoreCase', true);
end
