import os

import numpy as np

from generate_data import generate_data
from plot_q12 import plot_q12
from solve_q12 import solve_case1, solve_case2, solve_case3


def _format_float(value):
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "nan"
    return f"{value:.6g}"


def main():
    A, x_bar, b_bar, y_bar = generate_data()

    results = [
        solve_case1(A, y_bar),
        solve_case2(A, y_bar),
        solve_case3(A, y_bar),
    ]

    print("\nCase | Status               | Objective       | L1 norm       | Min        | Max")
    print("-" * 86)
    for idx, result in enumerate(results, start=1):
        status = result["status"]
        obj = result["objective"]
        x_val = result["x"]

        if x_val is not None:
            x_vec = np.asarray(x_val).reshape(-1)
            l1 = np.sum(np.abs(x_vec))
            x_min = x_vec.min()
            x_max = x_vec.max()
        else:
            l1 = np.nan
            x_min = np.nan
            x_max = np.nan

        print(
            f"{idx:^4} | {status:<19} | {_format_float(obj):<14} | "
            f"{_format_float(l1):<12} | {_format_float(x_min):<10} | {_format_float(x_max):<10}"
        )

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(project_root, "results")
    output_path = plot_q12(results, results_dir)
    print(f"\nSaved plot: {output_path}")


if __name__ == "__main__":
    main()
