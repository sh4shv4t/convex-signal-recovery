function [A, x_true, b_bar, y_bar] = generate_data()
%GENERATE_DATA Create synthetic data for convex signal recovery.
%   Returns A, x_true, b_bar, and y_bar with fixed random seed.

    rng(42); % reproducibility
    m = 100; n = 150;
    A = randn(m, n);

    % x_true: nonzero with probability 0.4
    mask = rand(n, 1) < 0.4;
    x_true = mask .* randn(n, 1);

    b_bar = randn(m, 1);
    y_bar = A * x_true + b_bar;
end
