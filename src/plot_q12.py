import os

import matplotlib.pyplot as plt
import numpy as np


def plot_q12(results, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    if not isinstance(axes, np.ndarray):
        axes = np.asarray([axes])

    for idx, ax in enumerate(axes, start=1):
        result = results[idx - 1]
        status = result["status"]
        x_val = result["x"]

        ax.set_title(f"Case {idx}")
        ax.set_ylabel("Value")
        ax.grid(True, alpha=0.3)

        if status in {"optimal", "optimal_inaccurate"} and x_val is not None:
            x_vec = np.asarray(x_val).reshape(-1)
            markerline, stemlines, baseline = ax.stem(x_vec, linefmt="C0-", markerfmt="C0.")
            plt.setp(baseline, color="0.7", linewidth=0.8)
        else:
            ax.text(
                0.5,
                0.5,
                f"{status}",
                transform=ax.transAxes,
                ha="center",
                va="center",
                fontsize=12,
            )

    axes[-1].set_xlabel("Index")
    fig.tight_layout()

    output_path = os.path.join(output_dir, "q12_cases.png")
    fig.savefig(output_path, dpi=150)
    return output_path
