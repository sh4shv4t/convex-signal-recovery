import numpy as np


def generate_data(seed=42, m=100, n=150, nonzero_prob=0.4):
    """Generate synthetic data for convex signal recovery."""
    np.random.seed(seed)
    A = np.random.randn(m, n)

    mask = (np.random.rand(n, 1) < nonzero_prob).astype(float)
    x_bar = mask * np.random.randn(n, 1)

    b_bar = np.random.randn(m, 1)
    y_bar = A @ x_bar + b_bar
    return A, x_bar, b_bar, y_bar
