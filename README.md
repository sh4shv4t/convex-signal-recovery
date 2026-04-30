# convex-signal-recovery
A CVX-based study of entropy-regularized signal recovery under linear constraint regimes.

![MATLAB](https://img.shields.io/badge/MATLAB-R2022a%2B-blue?logo=mathworks)
![CVX](https://img.shields.io/badge/CVX-2.2-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Contributors](https://img.shields.io/badge/contributors-3-blueviolet)

## Problem Statement
We solve the convex program $\min_{x \in \mathbb{R}^n} \sum_i x_i$ subject to three distinct feasibility sets: (1) $A x = b$, (2) $A x \ge b$, and (3) $A x \ge b$ with box bounds $-1 \le x_i \le 1$. The objective serves as a negative-entropy proxy while emphasizing sparse, low-complexity solutions.

## Methodology
The project uses CVX to implement disciplined convex programming (DCP) formulations. Each constraint regime is solved independently to compare feasibility, boundedness, and recovered signal structure.

## Results Summary
| Case | Constraint | Objective Value | CVX Status |
|------|------------|-----------------|-----------|
| 1 | $A x = b$ | Run `src/main.m` | Run `src/main.m` |
| 2 | $A x \ge b$ | Run `src/main.m` | Run `src/main.m` |
| 3 | $A x \ge b$, $-1 \le x_i \le 1$ | Run `src/main.m` | Run `src/main.m` |

## How to Run
1. Install MATLAB R2022a+ and CVX 2.2.
2. In MATLAB, add CVX to the path and run `cvx_setup` once.
3. Open the project folder and add `src/` to your MATLAB path.
4. Run `main.m` from the `src/` folder.

## File Structure
```
convex-signal-recovery/
├── README.md
├── LICENSE
├── src/
│   ├── main.m
│   ├── generate_data.m
│   ├── solve_case1.m
│   ├── solve_case2.m
│   ├── solve_case3.m
│   └── plot_results.m
├── results/
│   └── .gitkeep
└── docs/
    └── report.md
```

## Authors
- Shashvat Singh 
- Ankan Patra 
- Prince Kumar 

## References
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*
- CVX Research, *CVX Users' Guide and Documentation*
