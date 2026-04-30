function plot_results(x1, x2, x3, obj_vals, statuses)
%PLOT_RESULTS Visualize solution vectors and objective values.
%   Saves per-case figures and shows an objective comparison table.

    src_dir = fileparts(mfilename('fullpath'));
    project_root = fullfile(src_dir, '..');
    results_dir = fullfile(project_root, 'results');
    if ~exist(results_dir, 'dir')
        mkdir(results_dir);
    end

    x_cases = {x1, x2, x3};
    case_titles = {'Case 1', 'Case 2', 'Case 3'};

    for i = 1:3
        x = x_cases{i};
        if any(~isfinite(x))
            warning('%s has invalid values; skipping plot.', case_titles{i});
            continue;
        end

        fig = figure('Color', 'w', 'Name', case_titles{i});
        tiledlayout(2, 1, 'Padding', 'compact', 'TileSpacing', 'compact');

        nexttile;
        bar(x, 'FaceColor', [0.2 0.4 0.6]);
        title(sprintf('%s: Bar plot of x', case_titles{i}));
        ylabel('Value');
        grid on;

        nexttile;
        stem(x, 'Marker', '.', 'LineStyle', 'none');
        title('Sparsity (stem)');
        xlabel('Index');
        ylabel('Value');
        grid on;

        save_path = fullfile(results_dir, sprintf('case%d.png', i));
        exportgraphics(fig, save_path, 'Resolution', 150);
    end

    % Objective comparison table
    fig = figure('Color', 'w', 'Name', 'Objective Comparison');
    t = table((1:3)', obj_vals(:), statuses(:), ...
        'VariableNames', {'Case', 'ObjectiveValue', 'CVXStatus'});
    uitable('Data', t{:,:}, 'ColumnName', t.Properties.VariableNames, ...
        'Units', 'normalized', 'Position', [0 0 1 1]);
end
