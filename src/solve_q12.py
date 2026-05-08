import warnings

import cvxpy as cp
import numpy as np


def _print_solution_stats(label, prob, x_var):
    print(f"{label} status: {prob.status}")
    print(f"{label} objective: {prob.value}")
    if x_var.value is None:
        return
    x_val = np.asarray(x_var.value).reshape(-1)
    print(f"{label} l1: {np.sum(np.abs(x_val))}")
    print(f"{label} min: {x_val.min()}")
    print(f"{label} max: {x_val.max()}")


def solve_case1(A, y_bar):
    n = A.shape[1]
    x = cp.Variable((n, 1))
    prob = cp.Problem(cp.Minimize(cp.sum(x)), [A @ x == y_bar])
    prob.solve()
    _print_solution_stats("Case 1", prob, x)
    return {"x": x.value, "objective": prob.value, "status": prob.status}


def solve_case2(A, y_bar):
    n = A.shape[1]
    x = cp.Variable((n, 1))
    prob = cp.Problem(cp.Minimize(cp.sum(x)), [A @ x >= y_bar])
    prob.solve()
    _print_solution_stats("Case 2", prob, x)

    if prob.status not in {"unbounded", "unbounded_inaccurate"}:
        warnings.warn("Case 2 is expected to be unbounded without box bounds.")

    return {"x": x.value, "objective": prob.value, "status": prob.status}


def solve_case3(A, y_bar):
    n = A.shape[1]
    x = cp.Variable((n, 1))
    constraints = [A @ x >= y_bar, x >= -1, x <= 1]
    prob = cp.Problem(cp.Minimize(cp.sum(x)), constraints)
    prob.solve()
    _print_solution_stats("Case 3", prob, x)

    assert prob.status == "optimal", "Case 3 should be optimal and bounded."
    return {"x": x.value, "objective": prob.value, "status": prob.status}
